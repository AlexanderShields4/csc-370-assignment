import heapq


from puzzle import GOAL, PuzzleBoard
# h1 Misplaced tiles


def h1(board):

    count = 0
    for i in range(9):
        if board.state[i] != 0 and board.state[i] != GOAL[i]:
            count += 1

    return count


# h2 Manthatten Distance
# reminder: incase of negative


def h2(board):

    distance = 0
    for i in range(9):
        tile = board.state[i]
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


# A*
def astar(start_board, heuristic, stats=None):
    start_state = tuple(start_board.state)

    # f(n) = g(n) + h(n)
    start_g = 0
    start_h = heuristic(start_board)
    start_f = start_g + start_h

    priority_queue = [(start_f, start_state)]

    g_cost = {start_state: 0}

    came_from: dict[tuple[int, ...], tuple[int, ...] | None] = {
        start_state: None
    }

    states_expanded = 0

    while priority_queue:
        current_f, current_state = heapq.heappop(priority_queue)

        current_board = PuzzleBoard(list(current_state))
        current_g = g_cost[current_state]

        expected_f = current_g + heuristic(current_board)

        if current_f != expected_f:
            continue

        if current_board.is_goal():
            path = []
            path_state = current_state

            while path_state is not None:
                path.append(list(path_state))
                path_state = came_from[path_state]

            path.reverse()

            if stats is not None:
                stats["states_expanded"] = states_expanded
                stats["states_discovered"] = len(g_cost)

            return path

        states_expanded += 1

        for neighbor in current_board.get_neighbors():
            neighbor_state = tuple(neighbor.state)

            neighbor_g = current_g + 1

            if neighbor_state not in g_cost or neighbor_g < g_cost[neighbor_state]:
                g_cost[neighbor_state] = neighbor_g
                came_from[neighbor_state] = current_state

                neighbor_h = heuristic(neighbor)
                # f(n) = g(n) + h(n)
                neighbor_f = neighbor_g + neighbor_h

                heapq.heappush(priority_queue, (neighbor_f, neighbor_state))

    if stats is not None:
        stats["states_expanded"] = states_expanded
        stats["states_discovered"] = len(g_cost)

    return None
