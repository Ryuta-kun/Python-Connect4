#!/usr/bin/python
import sys, getopt, pickle
from p4_engine import blah

def main(argv):
  length = 3;
  width = 3;
  win = 3;
  try: 
    opts, args = getopt.getopt(sys.argv[1:], 'hl:w:d:', ['row=', 'column=', 'win='])
    if not opts:
      print 'No options supplied'
      print 'p4_main.py -l <row> -w <column> -d <win>'
      sys.exit(2)
  except getopt.GetoptError as err:
    print str(err)
    print 'p4_main.py -l <row> -w <column> -d <win>'
    sys.exit(2)
  try:
    for o, arg in opts:
      if o == '-h':
        print 'p4_main.py -l <row> -w <column> -d <win>'
        sys.exit(2)
      elif o in ('-l', '--row'):
        length = int(arg)
      elif o in ('-w', '--column'):
        width = int(arg)
      elif o in ('-d', '--win'):
        win = int(arg)
      else:
        assert False, "Unhandled option"
  except ValueError:
    print 'Please input numeric values'
    sys.exit(2)

  turn = 0
  thelist = [[-1 for x in range(length)] for x in range(width)]
  
  for i in thelist:
    for j in i:
      if j == -1:
        print '.\t',
      else:
        print '%d\t' %(j),
    print ''
  
  while blah().winner(length,width,win,thelist) == -1:
    try:
      userIn = raw_input("Player %d Turn: " % (turn+1))
      data = int(userIn)
      num = blah().placeToken(turn, data, length, width, thelist)
      
      if num != -1:
        turn = 1 if turn == 0 else 0
        for i in thelist:
          for j in i:
            if j == -1:
              print '.\t',
            else:
              print '%d\t' %(j),
          print ''
    except ValueError:
      try:
        userSplit = userIn.split(" ",1)
        if userSplit[0] == '-h':
            print '-s <save> or -l <load> or -q <quit>'
        elif userSplit[0] in ('-l', '--load'):
          fileObject = open(userSplit[1],'rb')
          length = pickle.load(fileObject)
          width = pickle.load(fileObject)
          win = pickle.load(fileObject)
          thelist = pickle.load(fileObject)
          turn = pickle.load(fileObject)
        elif userSplit[0] in ('-s', '--save'):
          fileObject = open(userSplit[1],'wb')
          pickle.dump(length, fileObject)
          pickle.dump(width, fileObject)
          pickle.dump(win, fileObject)
          pickle.dump(thelist,fileObject)
          pickle.dump(turn, fileObject)
          fileObject.close()
        elif userSplit[0] in ('-q', '--quit'):
          useQ = raw_input("Are you sure you want to quit <yes or no>: ")
          if useQ == 'yes':
            sys.exit(2)
        else:
          print "Unhandled option"
      except IOError:
        print "File not found."
      except IndexError:
        print "You must enter the file name."

if __name__ == "__main__":
  main(sys.argv[1:])


