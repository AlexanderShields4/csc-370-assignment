# CSC 370 Homework 1: A* on the 8-puzzle

This repository implements A* search for the 8-puzzle and compares three admissible heuristics. The experiment follows the assignment's Russell and Norvig Figure 3.29 comparison: run problems with known solution depths and measure search effort and effective branching factor.

## Requirements

- Python 3.10 or newer

## Run the programs

From the repository root, run the full experiment (100 puzzles at each even solution depth from 2 through 24):

```sh
python3 -B src/test.py
```

The script prints the mean number of states expanded and mean effective branching factor for h1, h2, and h3 at each depth. It uses only the Python standard library. `-B` prevents Python from writing bytecode files into the repository.

To test one puzzle directly, start Python in `src` and call the existing A* function:

```python
from astar import astar, h2
from puzzle import GOAL, PuzzleBoard

path = astar(PuzzleBoard([1, 2, 3, 4, 5, 6, 0, 7, 8]), h2)
print("Moves:", len(path) - 1)  # 2
print("Reached goal:", path[-1] == GOAL)  # True
```

## Experiment design

The goal state is `[1, 2, 3, 4, 5, 6, 7, 8, 0]`. For each requested depth, `src/test.py` runs breadth-first search from the goal to build the set of states at that exact shortest-path depth. It samples 100 states from each depth's set, with replacement, using random seed `370`. Thus every selected puzzle is solvable and its optimal solution length is known before A* runs.

Each sampled board is solved with all three heuristics:

- **h1:** number of misplaced numbered tiles
- **h2:** sum of the numbered tiles' Manhattan distances to their goal squares
- **h3:** Manhattan distance plus two moves for each minimum tile removal needed to resolve row and column linear conflicts

The h3 heuristic follows Hansson, Mayer, and Yung, “Generating Admissible Heuristics by Criticizing Solutions to Relaxed Models” (1985), [doi:10.7916/D89Z9CW3](https://doi.org/10.7916/D89Z9CW3).

## Measurements

`states_expanded` counts non-goal states removed from A*'s priority queue and expanded. For each puzzle, the program computes effective branching factor `b*` from:

```text
N + 1 = 1 + b* + (b*)^2 + ... + (b*)^d
```

Here `N` is the number of states expanded and `d` is the known optimal solution depth. It then reports the mean node count and the mean of the per-puzzle `b*` values at each depth. The primary comparison is how the heuristics reduce expansions and `b*` as depth increases; elapsed time is not used as the main measure.

The experiment uses A* graph search, storing the best known path cost per board state. Equal-priority states are ordered by their board-state tuples. These choices, along with the sampled puzzles and the precise node-count definition, should be kept in mind when comparing results with Russell and Norvig.

## Code layout

- `src/puzzle.py` defines the goal state and the `PuzzleBoard` representation and moves.
- `src/astar.py` defines A*, h1, h2, and h3.
- `src/test.py` generates exact-depth boards, compares heuristics, and runs the repeated experiment.
