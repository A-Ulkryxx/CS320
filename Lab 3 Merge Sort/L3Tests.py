from main import mergesort

# None
assert(mergesort(None) == None)

# Empty List
assert(mergesort([]) == [])

# Duplicates
assert(mergesort([7, 4, 3, 1, 7]) == [1, 3, 4, 7, 7])
assert(mergesort([7, 4, 7, 1, 3]) == [1, 3, 4, 7, 7])
assert(mergesort([3, 4, 7, 1, 7]) == [1, 3, 4, 7, 7])
assert(mergesort([3, 4, 3, 7, 1, 7]) == [1, 3, 3, 4, 7, 7])

# Standard inputs
assert(mergesort([6, 5, 2, 8, 10, 1, 4, 3]) == [1, 2, 3, 4, 5, 6, 8, 10])

# Pre-Sorted List
assert(mergesort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6])

# Reverse Sorted List
assert(mergesort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6])

# Same element
assert(mergesort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1])