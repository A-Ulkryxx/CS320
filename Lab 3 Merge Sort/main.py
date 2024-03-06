

def seperate_list(mlist):
    mid_i = len(mlist) // 2
    return mlist[mid_i:], mlist[:mid_i]


def sort_split(mlist):
    list_length = len(mlist)
    if (list_length > 1):
        left_sect, right_sect = seperate_list(mlist)
        left_sect = sort_split(left_sect)
        right_sect = sort_split(right_sect)
        sort_comparison(left_sect, right_sect, mlist)
    return mlist


def sort_comparison(left_sect, right_sect, mlist):
    i = 0
    j = 0
    n = 0
    left_length = len(left_sect)
    right_length = len(right_sect)
    while ((i < left_length) and (j < right_length)):
        if left_sect[i] <= right_sect[j]:
            mlist[n] = left_sect[i]
            i += 1
        else:
            mlist[n] = right_sect[j]
            j += 1
        n += 1
    while ((i < left_length) or (j < right_length)):
        if (i < left_length):
            mlist[n] = left_sect[i]
            i += 1
        else:
            mlist[n] = right_sect[j]
            j += 1
        n += 1
    return mlist


def mergesort(mlist):
    if mlist is None:
        return None
    if (mlist == []):
        return []
    return sort_split(mlist)
