#h1 Misplaced tiles

def h1 (board):

  count = 0
  for i in range (9):

    if board.state[i] != 0 and board.state[i] != GOAL[i]:

      count += 1
  
  return count

#h2 Manthatten Distance

def h2 (board):

  distance = 0
  for i in range (9):
    

#A*
