

def is_not_list(elem):
    return type(elem) is not list


def get_rows_and_cols(torus):
    rows = len(torus)
    cols = len(torus[0])
    return rows, cols


def get_num_elems(torus):
    m, n = get_rows_and_cols(torus)
    return m * n


def get_neighbors(torus, i, j):
    u_d_l_r_neighbors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    rows, cols = get_rows_and_cols(torus)
    ind_m = rows - 1
    ind_n = cols - 1
    if (ind_m == 0):
        return [[0, y] for y in range(0, cols)]
    elif (ind_n == 0):
        return [[x, 0] for x in range(0, rows)]
    if i == 0:
        u_d_l_r_neighbors[0][0] = ind_m
    elif i == ind_m:
        u_d_l_r_neighbors[1][0] = 0
    if j == 0:
        u_d_l_r_neighbors[2][1] = ind_n
    elif j == ind_n:
        u_d_l_r_neighbors[3][1] = 0
    return u_d_l_r_neighbors


def get_all_trails(torus, i, j, ind_matrix, v_indices):
    if (ind_matrix[i][j] != -1):
        return ind_matrix[i][j]
    trail_path = [(i, j)]
    v_indices[0] += 1
    neighbors = get_neighbors(torus, i, j)
    current = torus[i][j]
    possible_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        next_value = torus[row][col]
        if (next_value > current):
            temp_trail = trail_path + \
                get_all_trails(torus, row, col, ind_matrix, v_indices)
            if (ind_matrix[i][j] == -1):
                ind_matrix[i][j] = temp_trail
            elif (len(temp_trail) > len(ind_matrix[i][j])):
                ind_matrix[i][j] = temp_trail
            possible_neighbors.append(neighbor)
    if possible_neighbors == []:
        ind_matrix[i][j] = trail_path
        return trail_path
    return ind_matrix[i][j]


def get_longest_trail(torus):
    longest_len = 0
    long_i = 0
    long_j = 0
    v_indices = [0]
    num_elems = get_num_elems(torus)
    rows, cols = get_rows_and_cols(torus)
    ind_matrix = [[-1] * cols for x in range(0, rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            length = len(get_all_trails(torus, i, j, ind_matrix, v_indices))
            if (length > longest_len):
                longest_len = length
                long_i = i
                long_j = j
            if (v_indices[0] == num_elems):
                return ind_matrix[long_i][long_j]
    return ind_matrix[long_i][long_j]


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
    num_elems = get_num_elems(torus)
    if (num_elems < 2):
        return []
    trail = get_longest_trail(torus)
    if (len(trail) < 2):
        return []
    return trail
