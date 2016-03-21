#!/usr/bin/python
class blah:

  def placeToken(self, player, column, numrow, numcolumn, thelist):
    if player == 0 or player == 1:
      if column >= 0 and column < numcolumn and numrow >= 3 and numcolumn >= 3:
        for i in xrange(numrow-1, -1, -1):
          if thelist[i][column] == -1:
            thelist[i][column] = player
            return 0
          if i == 0 and thelist[i][column] != -1:
            print "The column is full, please try another."
      else:
        print "Please Enter a valid value."
    else:
      print "That player doesnt exist."
    return -1

  def winner(self, numrow, numcolumn, win, thelist):
    if win >= 3 and win <= numrow and win <= numcolumn:
      for p in xrange(2): 
        for i in xrange(numrow):
          for j in xrange(numcolumn):
            horiz = blah().horizontalCheck(p,i,j,numrow,numcolumn,win,thelist)
            vert = blah().verticalCheck(p,i,j,numrow,numcolumn,win,thelist)
            neg = blah().negativeCheck(p,i,j,numrow,numcolumn,win,thelist)
            pos = blah().positiveCheck(p,i,j,numrow,numcolumn,win,thelist)
            if horiz == p or vert == p or neg == p or pos == p:
              print "Player ", p, " is the winner"
              return p
            if blah().tieGame(thelist) == -2:
              print "The game ends in a Tie. Please reset the board."
              return -2
      return -1
    else:
      print "The length to win must be greater than 3 and less than or equal to the board size."
      return -3

  def horizontalCheck(self, i, r, j, numrow, numcolumn, win, thelist):
    c=0
    while (j+c) < numcolumn and thelist[r][j + c] == i:
      if((c+1) == win):
        return i
      c+=1
    return -1

  def verticalCheck(self, i, r, j, numrow, numcolumn, win, thelist):
    c=0
    while (r+c) < numrow and thelist[r+c][j] == i:
      if((c+1) == win):
        return i
      c+=1
    return -1

  def negativeCheck(self, i, r, j, numrow, numcolumn, win, thelist):
    c=0
    while (r+c) < numrow and (j+c) < numcolumn and thelist[r+c][j + c] == i:
      if((c+1) == win):
        return i
      c+=1
    return -1

  def positiveCheck(self, i, r, j, numrow, numcolumn, win, thelist):
    c=0
    while (r+c) < numrow and (j-c) > -1 and thelist[r + c][j - c] == i:
      if((c+1) == win):
        return i
      c+=1
    return -1

  def tieGame(self, thelist):
    for i in thelist:
      for j in i:
        if j == -1:
          return -1
    return -2
