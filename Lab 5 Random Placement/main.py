

import random


def get_map_dimensions(map):
    if type(map[0]) is not tuple:
        return 1, 0
    return len(map), len(map[0])


def get_num_map_spots(map):
    dim_L, dim_S = get_map_dimensions(map)
    if dim_L == 1:
        return 0
    return dim_L * dim_S


def check_row_len_inequality(map):
    dim_L = get_map_dimensions(map)[0]
    for i in range(1, dim_L):
        if len(map[0]) != len(map[i]):
            return True
    return False


def get_free_spaces(map):
    free_spaces = []
    dim_L, dim_S = get_map_dimensions(map)
    for i in range(0, dim_L):
        for j in range(0, dim_S):
            if map[i][j] is True:
                free_spaces.append((i, j))
    return free_spaces


def place_objects(num_objects, free_spaces):
    placed_objs = []
    for object in range(0, num_objects):
        placement = random.choice(free_spaces)
        free_spaces.remove(placement)
        placed_objs.append(placement)
    return placed_objs


def placement(num_objects, map):
    if (type(num_objects) is not int) or (num_objects < 1):
        return None
    if (map is None) or (map == ()) or (map[0] == ()):
        return None
    if get_num_map_spots(map) == 0:
        return None
    if check_row_len_inequality(map):
        return None
    free_spaces = get_free_spaces(map)
    num_P = len(free_spaces)
    if (num_P <= 0) or (num_P < num_objects):
        return None
    return place_objects(num_objects, free_spaces)
