

def visited(trail, tup):
    return (tup in trail)


def is_not_list(elem):
    return type(elem) is not list


def get_rows_and_cols(torus):
    rows = len(torus)
    cols = len(torus[0])
    return rows, cols


def get_num_elems(torus):
    m, n = get_rows_and_cols(torus)
    return m * n


def get_index_dimensions(torus):
    ind_m = len(torus) - 1
    ind_n = len(torus[0]) - 1
    return ind_m, ind_n


def get_neighbors(torus, i, j):
    neighbors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    ind_m, ind_n = get_index_dimensions(torus)
    rows, cols = get_rows_and_cols(torus)
    if (ind_m == 0):
        return [[0, y] for y in range(0, cols)]
    elif (ind_n == 0):
        return [[x, 0] for x in range(0, rows)]
    if i == 0:
        neighbors[0][0] = ind_m
    elif i == ind_m:
        neighbors[1][0] = 0
    if j == 0:
        neighbors[2][1] = ind_n
    elif j == ind_n:
        neighbors[3][1] = 0
    return neighbors


def next_neighbor(torus, trail, neighbors, current):
    possible_elems = []
    possible_neighbors = []
    for neighbor in neighbors:
        row, column = neighbor
        next_value = torus[row][column]
        if ((not visited(trail, neighbor)) and (next_value > current)):
            possible_elems.append(next_value)
            possible_neighbors.append(neighbor)
    if possible_elems == []:
        return None
    next_elem = min(possible_elems)
    temp_ind = possible_elems.index(next_elem)
    next_indices = possible_neighbors[temp_ind]
    return next_indices


def find_trail(torus, i, j, trail):
    trail.append((i, j))
    current = torus[i][j]
    neighbors = get_neighbors(torus, i, j)
    next_indices = next_neighbor(torus, trail, neighbors, current)
    if next_indices is None:
        trail_len = len(trail)
        return trail_len
    next_i, next_j = next_indices
    trail_len = find_trail(torus, next_i, next_j, trail)
    return trail_len


def get_longest_trail(torus):
    longest_trail = []
    longest_len = 0
    rows, cols = get_rows_and_cols(torus)
    ind_tracker = [[-1] * cols for x in range(0, rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            trail = []
            if ind_tracker[i][j] == -1:
                ind_tracker[i][j] = find_trail(torus, i, j, trail)
            if ind_tracker[i][j] > longest_len:
                longest_len = ind_tracker[i][j]
                longest_trail = trail
    if (longest_len < 2):
        return []
    return longest_trail


def longest_path(torus):
    if torus is None:
        return []
    if (torus == []):
        return []
    if (torus[0] == []):
        return []
    first_elem = torus[0]
    if (is_not_list(first_elem)):
        return []
    num_elem = get_num_elems(torus)
    if (num_elem < 2):
        return []
    return get_longest_trail(torus)
