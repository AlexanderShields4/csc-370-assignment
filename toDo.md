# Homework progress tracker based on the hw1 doc

[] design 8 puzzle board, write and debug the code for manipulating
and testing the puzzle
[] implement and debug A*. compare it to Russel and Norvigs results.
[] Complete experiments think about the presentation narrative
[] finalize the slide deck

## Notes from Russell and Norvig's results

- branching factor: When the empty tile is in the middle, four moves are possible, when it is in a corner, two and when it is an edge, three.

- Effective branching factor: standardized efficiency score for a heuristic.

- If A*finds a solution at depth $d$ after generating $N$ total nodes, $b^*$ calculates what branching factor a perfectly uniform search tree of depth $d$ would need to contain that same number of nodes ($N + 1$, including the root node). example decoded: d = 5, N = 52, 52 + 1 = 1 + b* + (b*)^2 + (b*)^3 + (b*)^4 + (b*)^5. result b* = 1.92

- Russell and Norvigs generated 1200 random problems with solution lengths from 2 to 24. their results suggest that h2, the sum of distances of the tiles from their goal positions, is a better heuristic than h1, the number of misplaced tiles. heuristic for a relaxed problem is admisable for the real problem because the optimized version only adds edges that can

Relaxed problem for h2: a) A tile can move from square A to square B if A is adjacent to B
Relaxed problem for h1: c) A tile can move from square A to square B

Admissible heuristics can also be derived from the solution cost of a subproblem. this is the idea behind pattern data bases -- store the exact solution costs for every possible subproblem instance
