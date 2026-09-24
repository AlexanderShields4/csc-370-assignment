import random

from astar import astar, h1, h2, h3
from puzzle import GOAL, PuzzleBoard


def make_depth_level(target_depth):
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

    return current_level


def make_random_board(target_depth):
    random_state = random.choice(make_depth_level(target_depth))
    return PuzzleBoard(random_state.copy())


def compare_heuristics(target_depth=None, board=None, show_results=True):
    if target_depth is None:
        target_depth = random.randint(2, 24)
    if board is None:
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

    results = h1_stats, h2_stats, h3_stats
    if not show_results:
        return results

    print("This puzzle requires", target_depth, "moves to solve:")
    board.display()

    print(f"{'':<20}{'h1':>12}{'h2':>12}{'h3':>12}")
    print(f"{'Starting value':<20}{h1(board):>12}{h2(board):>12}{h3(board):>12}")
    print(f"{'Solution moves':<20}{h1_moves:>12}{h2_moves:>12}{h3_moves:>12}")
    print(
        f"{'Nodes generated':<20}"
        f"{h1_stats['nodes_generated']:>12}"
        f"{h2_stats['nodes_generated']:>12}"
        f"{h3_stats['nodes_generated']:>12}"
    )
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

    return results


def effective_branching_factor(nodes, depth):
    low = 0.0
    high = nodes + 1.0

    for _ in range(50):
        middle = (low + high) / 2
        total = sum(middle ** level for level in range(depth + 1))

        if total < nodes + 1:
            low = middle
        else:
            high = middle

    return (low + high) / 2


def run_experiments(number_of_problems=100):
    random.seed(370)
    print(
        f"{'Depth':<8}"
        f"{'h1 generated':>12}{'h1 b*':>12}"
        f"{'h2 generated':>12}{'h2 b*':>12}"
        f"{'h3 generated':>12}{'h3 b*':>12}"
    )

    for depth in range(2, 25, 2):
        depth_level = make_depth_level(depth)
        totals = [[0, 0.0] for _ in range(3)]

        for _ in range(number_of_problems):
            state = random.choice(depth_level)
            board = PuzzleBoard(state.copy())
            results = compare_heuristics(depth, board, False)

            for index, stats in enumerate(results):
                nodes = stats["nodes_generated"]
                totals[index][0] += nodes
                totals[index][1] += effective_branching_factor(nodes, depth)

        print(
            f"{depth:<8}"
            f"{totals[0][0] / number_of_problems:>12.2f}"
            f"{totals[0][1] / number_of_problems:>12.2f}"
            f"{totals[1][0] / number_of_problems:>12.2f}"
            f"{totals[1][1] / number_of_problems:>12.2f}"
            f"{totals[2][0] / number_of_problems:>12.2f}"
            f"{totals[2][1] / number_of_problems:>12.2f}"
        )


if __name__ == "__main__":
    run_experiments()
