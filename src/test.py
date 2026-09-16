import random

from puzzle import GOAL, PuzzleBoard


def make_random_board(target_depth):
    current_level = [GOAL.copy()]

    # Remember every state BFS has already discovered
    visited = {tuple(GOAL)}

    # Build one complete level at a time
    for _ in range(target_depth):
        next_level = []

        for state in current_level:
            board = PuzzleBoard(state)

            for neighbor in board.get_neighbors():
                neighbor_key = tuple(neighbor.state)

                if neighbor_key not in visited:
                    visited.add(neighbor_key)
                    next_level.append(neighbor.state)

        current_level = next_level

    random_state = random.choice(current_level)
    return PuzzleBoard(random_state.copy())


target_depth = random.randint(2, 24)
board = make_random_board(target_depth)

print("This puzzle requires", target_depth, "moves to solve:")
board.display()
