from puzzle import PuzzleBoard
import random 

state = list(range(9))
random.shuffle(state)


board = PuzzleBoard(state)

print("Empty tile index:", board.find_empty())
print("Board layout:")
board.display()
