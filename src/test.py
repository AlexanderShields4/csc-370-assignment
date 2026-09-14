import random

from puzzle import PuzzleBoard

# Map of valid adjacent index swaps for a 3x3 grid
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}

state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Make between 2 and 24 random valid slides
for _ in range(random.randint(2, 24)):
    blank = state.index(0)
    swap = random.choice(MOVES[blank])
    state[blank], state[swap] = state[swap], state[blank]

board = PuzzleBoard(state)
board.display()

empty = board.find_empty()
newposition = random.choice(MOVES[empty])
board = board.move(empty, newposition)
board.display()
