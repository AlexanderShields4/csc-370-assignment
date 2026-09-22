import random

from astar import astar, h1, h2, h3
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


def compare_heuristics():
    target_depth = random.randint(2, 24)
    board = make_random_board(target_depth)

    h1_stats = {}
    h2_stats = {}
    h3_stats = {}

    h1_path = astar(board, h1, h1_stats)
    h2_path = astar(board, h2, h2_stats)
    h3_path = astar(board, h3, h3_stats)

    h1_moves = len(h1_path) - 1
    h2_moves = len(h2_path) - 1
    h3_moves = len(h3_path) - 1

    print("This puzzle requires", target_depth, "moves to solve:")
    board.display()

    print(f"{'':<20}{'h1':>12}{'h2':>12}{'h3':>12}")
    print(f"{'Starting value':<20}{h1(board):>12}{h2(board):>12}{h3(board):>12}")
    print(f"{'Solution moves':<20}{h1_moves:>12}{h2_moves:>12}{h3_moves:>12}")
    print(
        f"{'States expanded':<20}"
        f"{h1_stats['states_expanded']:>12}"
        f"{h2_stats['states_expanded']:>12}"
        f"{h3_stats['states_expanded']:>12}"
    )
    print(
        f"{'States discovered':<20}"
        f"{h1_stats['states_discovered']:>12}"
        f"{h2_stats['states_discovered']:>12}"
        f"{h3_stats['states_discovered']:>12}"
    )

    return h1_stats, h2_stats, h3_stats


if __name__ == "__main__":
    compare_heuristics()
