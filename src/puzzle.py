GOAL = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

class PuzzleBoard:

  
    def __init__(self, state):
        self.state = state

    def find_empty(self):
        return self.state.index(0)

    def display(self):
        for i in range(0, 9, 3):
            print(self.state[i : i + 3])
        print()

  # need to check goal state
    def is_goal(self):
      return self.state == GOAL

  #method to move blank

    def move(self, empty, newposition):

      newstate = self.state.copy()

      newstate[empty], newstate[newposition] = ( newstate[newposition], newstate[empty] )

      return PuzzleBoard(newstate)

  #record blank, check up, down, left, right

    def get_neighbors(self):
      
      neighbours = []

      empty = self.find_empty() 
      
      row = empty // 3
      col = empty % 3

      if row > 0:
        neighbours.append(self.move(self, empty - 3))

      if row < 2:
        neighbours.append(self.move(self, empty + 3))

      if col > 0:
        neighbors.append(self.move(empty, empty - 1))
       
      if col < 2:
        neighbors.append(self.move(empty, empty + 1))

      return neighbours
