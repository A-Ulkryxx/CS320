

def visited(trail, tup):
    return (tup in trail)


def is_not_list(elem):
    return type(elem) is not list


def get_index_dimensions(torus):
    m = len(torus) - 1
    n = len(torus[0]) - 1
    return m, n


def get_num_elems(torus):
    m = len(torus)
    n = len(torus[0])
    return m * n


def get_minimum_indices(torus):
    m, n = get_index_dimensions(torus)
    min_val = torus[0][0]
    min_row = 0
    min_col = 0
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if (torus[i][j] < min_val):
                min_val = torus[i][j]
                min_row = i
                min_col = j
    return min_row, min_col


def get_neighbors(torus, i, j):
    neighbors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    m, n = get_index_dimensions(torus)
    if (m == 0):
        return [[0, y] for y in range(0, n + 1)]
    if (n == 0):
        return [[x, 0] for x in range(0, m + 1)]
    if i == 0:
        neighbors[0][0] = m
    elif i == m:
        neighbors[1][0] = 0
    if j == 0:
        neighbors[2][1] = n
    elif j == n:
        neighbors[3][1] = 0
    return neighbors


def get_neighbor_indices(neighbor):
    return neighbor[0], neighbor[1]


def next_neighbor(torus, trail, neighbors, current):
    possible_elems = []
    possible_neighbors = []
    for neighbor in neighbors:
        row, column = get_neighbor_indices(neighbor)
        value = torus[row][column]
        temp_tup = (row, column)
        if ((not visited(trail, temp_tup)) and (value > current)):
            possible_elems.append(value)
            possible_neighbors.append(neighbor)
    if possible_elems == []:
        return None
    next_elem = min(possible_elems)
    # if( possible_elems.count(next_elem) > 1):
    temp_ind = possible_elems.index(next_elem)
    next_indices = possible_neighbors[temp_ind]
    path = (next_indices[0], next_indices[1])
    trail.append(path)
    return next_indices


def find_trail(torus):
    total_num_elem = get_num_elems(torus)
    trail = []
    i, j = get_minimum_indices(torus)
    trail.append((i, j))
    for k in range(0, total_num_elem):
        current = torus[i][j]
        neighbors = get_neighbors(torus, i, j)
        next_indices = next_neighbor(torus, trail, neighbors, current)
        if next_indices is None:
            break
        i = next_indices[0]
        j = next_indices[1]
    trail_len = len(trail)
    if (trail_len < 2):
        return []
    return trail


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
    return find_trail(torus)




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
        return [[0, y] for y in range(0,  cols)]
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


def get_neighbor_indices(neighbor):
    return neighbor[0], neighbor[1]


def next_neighbor(torus, trail, neighbors, current):
    possible_elems = []
    possible_neighbors = []
    for neighbor in neighbors:
        row, column = get_neighbor_indices(neighbor)
        value = torus[row][column]
        temp_tup = (row, column)
        if ((not visited(trail, temp_tup)) and (value > current)):
            possible_elems.append(value)
            possible_neighbors.append(neighbor)
    if possible_elems == []:
        return None
    next_elem = min(possible_elems)
    temp_ind = possible_elems.index(next_elem)
    next_indices = possible_neighbors[temp_ind]
    return next_indices


def find_trail(torus, i, j, ind_tracker, trail):
    if ind_tracker[i][j] != -1:
        return ind_tracker[i][j]
    trail.append((i, j))
    current = torus[i][j]
    neighbors = get_neighbors(torus, i, j)
    next_indices = next_neighbor(torus, trail, neighbors, current)
    if next_indices is None:
        ind_tracker[i][j] = len(trail)
        return ind_tracker[i][j]
    next_i, next_j = next_indices
    ind_tracker[i][j] = find_trail(torus, next_i, next_j, ind_tracker, trail)

    return ind_tracker[i][j]


def get_longest_trail(torus):
    longest_trail = []
    longest_len = 0
    rows, cols = get_rows_and_cols(torus)
    ind_tracker = [[-1] * cols for x in range(0, rows) ]
    for i in range(0, rows):
        for j in range(0, cols):
            trail = []
            trail_len = find_trail(torus, i, j, ind_tracker, trail)
            if trail_len > longest_len:
                longest_len = trail_len
                longest_trail = trail
    if (len(longest_trail) < 2):
        return []
    return longest_trail