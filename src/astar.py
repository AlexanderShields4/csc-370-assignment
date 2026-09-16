#h1 Misplaced tiles

def h1 (board):

  count = 0
  for i in range (9):

    if board.state[i] != 0 and board.state[i] != GOAL[i]:

      count += 1
  
  return count

#h2 Manthatten Distance
#reminder: incase of negative

def h2 (board):

  distance = 0
  for i in range (9):

    title = board.state[i]
    if tile == 0:
      continue

    currentRow = i // 3
    currentCol = i % 3
    
    goalIndex = GOAL.index(tile)
    goalRow = goalIndex // 3
    goalCol = goalIndex % 3
    
    distance += abs(currentRow - goalRow)
    distance += abs(currentCol - goalCol)
    
  return distance
    

#A*
