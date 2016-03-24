#!/usr/bin/python

import sys, pickle
from PyQt4 import QtGui, QtCore
from p4_engine import blah

class exampleGUI(QtGui.QWidget):
  turn = 0
  def __init__(self, row, column,win):
    super(exampleGUI, self).__init__()
    self.row = row
    self.column = column
    self.win = win
    self.initUI()
  def initUI(self):
    vbox = QtGui.QVBoxLayout()
    self.grid = QtGui.QGridLayout()
    self.thelist = [[-1 for x in xrange(self.column)] for x in xrange(self.row)]
    self.labels = [[-1 for x in xrange(self.column)] for x in xrange(self.row)]
    
    menubar = QtGui.QMenuBar(self)
    menubar.setNativeMenuBar(False)
    fileMenu = menubar.addMenu('&File')
    exitAction = QtGui.QAction('&Exit',self)
    exitAction.triggered.connect(QtGui.qApp.quit)
    fileMenu.addAction(exitAction)

    saveAction = QtGui.QAction('&Save',self)
    saveAction.setShortcut('Ctrl+S')
    saveAction.triggered.connect(self.saveDialog)
    fileMenu.addAction(saveAction)

    load = QtGui.QAction('&Open',self)
    load.setShortcut('Ctrl+O')
    load.triggered.connect(self.openDialog)
    fileMenu.addAction(load)
    vbox.addWidget(menubar, 0)

    for i in range(self.column):
      button = QtGui.QPushButton('%d' % i)
      button.setObjectName('%d' % i)
      button.clicked.connect(self.on_click)
      self.grid.addWidget(button, 1, i)

    for i in range(self.row):
      for j in range(self.column):
        self.labels[i][j] = QtGui.QLabel('.')
        self.labels[i][j].setAlignment(QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.labels[i][j], i+2, j)
    
    vbox.addLayout(self.grid) 
    self.setLayout(vbox)
    self.setGeometry(300,300,250,150)
    self.setStyleSheet("background-color:white;")
    self.setWindowTitle('Connect4 in Python')
    self.show() 

  def on_click(self):
    sending_button = self.sender()
    column = int(sending_button.objectName())
    num = blah().placeToken(exampleGUI.turn,column,self.row,self.column,self.thelist)
    
    if num != -1:
      exampleGUI.turn = 1 if exampleGUI.turn == 0 else 0
      for x in xrange(self.row):
        for y in xrange(self.column):
          if self.thelist[x][y] <> -1:
            self.labels[x][y].setText('%d' % self.thelist[x][y])
    winner = blah().winner(self.row, self.column, self.win, self.thelist)
    
    if winner == 0 or winner == 1:
       msg = QtGui.QMessageBox.information(self, 'Message', "Player %d is the winner!!" % (winner+1), QtGui.QMessageBox.Ok)
       if msg == QtGui.QMessageBox.Ok:
         sys.exit(2)
    elif winner == -2:
       msg = QtGui.QMessageBox.information(self, 'Message', "The game is a Tie", QtGui.QMessageBox.Ok)
       if msg == QtGui.QMessageBox.Ok:
         sys.exit(2)
      
  def saveDialog(self):
    try:
      fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '/home/hiranor')
      fileObject = open(fname,'wb')
      pickle.dump(self.row, fileObject)
      pickle.dump(self.column, fileObject)
      pickle.dump(self.win, fileObject)
      pickle.dump(self.thelist,fileObject)
      pickle.dump(exampleGUI.turn, fileObject)
      fileObject.close()
    except IOError:
      print "File not found."
    except IndexError:
      print "You must enter the file name."
      sys.exit(2)
  def openDialog(self):
    try:
      fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/hiranor')
      f = open(fname, 'r')
      self.row = pickle.load(f)
      self.column = pickle.load(f)
      self.win = pickle.load(f)
      self.thelist = pickle.load(f)
      exampleGUI.turn = pickle.load(f)
      self.repaint()
      self.labels = [[-1 for x in xrange(self.column)] for x in xrange(self.row)]
    
      for i in range(self.column):
        button = QtGui.QPushButton('%d' % i)
        button.setObjectName('%d' % i)
        button.clicked.connect(self.on_click)
        self.grid.addWidget(button, 1, i)

      for i in range(self.row):
        for j in range(self.column):
          self.labels[i][j] = QtGui.QLabel('.')
          self.labels[i][j].setAlignment(QtCore.Qt.AlignCenter)
          self.grid.addWidget(self.labels[i][j], i+2, j)
    
      for x in xrange(self.row):
        for y in xrange(self.column):
          if self.thelist[x][y] <> -1:
            self.labels[x][y].setText('%d' % self.thelist[x][y])

    except IOError:
      print "File not found."
    except IndexError:
      print "You must enter the file name."
      sys.exit(2)
    except KeyError:
      print "Incorrect File."
