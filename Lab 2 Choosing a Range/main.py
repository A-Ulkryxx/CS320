# Austin Youngren
# Lab 2: extract values from a sorted list


def get_lo(list_s, lo_i, mid_i, hi_i, lo):
    if (lo_i >= hi_i):
        return lo_i
    elif (list_s[mid_i] >= lo):
        hi_i = mid_i
        mid_i = (lo_i + hi_i) // 2
        lo_i = get_lo(list_s, lo_i, mid_i, hi_i, lo)
    else:
        lo_i = mid_i + 1
        mid_i = (lo_i + hi_i) // 2
        lo_i = get_lo(list_s, lo_i, mid_i, hi_i, lo)
    return lo_i


def get_hi(list_s, lo_i, mid_i, hi_i, hi):
    if (lo_i >= hi_i):
        return lo_i
    elif (hi < list_s[mid_i]):
        hi_i = mid_i
        mid_i = (lo_i + hi_i) // 2
        lo_i = get_hi(list_s, lo_i, mid_i, hi_i, hi)
    else:
        lo_i = mid_i + 1
        mid_i = (lo_i + hi_i) // 2
        lo_i = get_hi(list_s, lo_i, mid_i, hi_i, hi)
    return lo_i


def extract(list_s, lo, hi):
    if list_s is None:
        return None
    if (list_s == []):
        return list_s

    list_length = len(list_s)
    lo_i = 0
    hi_i = list_length
    mid_i = (lo_i + hi_i) // 2

    if (lo is None and hi is None):
        return list_s
    elif lo is None:
        hi_pointer = get_hi(list_s, lo_i, mid_i, hi_i, hi)
        return list_s[0: hi_pointer]
    elif hi is None:
        lo_pointer = get_lo(list_s, lo_i, mid_i, hi_i, lo)
        return list_s[lo_pointer: list_length]

    if (lo > hi):
        return None

    hi_pointer = get_hi(list_s, lo_i, mid_i, hi_i, hi)
    lo_pointer = get_lo(list_s, lo_i, mid_i, hi_i, lo)

    return list_s[lo_pointer: hi_pointer]
