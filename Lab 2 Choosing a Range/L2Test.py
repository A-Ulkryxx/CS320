from main import extract

# List None
assert(extract(None, 1, 10) == None)

# lo greater than high
assert(extract([1, 2, 3, 4, 4], 10, 1) == None)
assert(extract([], 1, 10) == [])

#lo is None
assert(extract([1, 2, 3, 4, 4], None, 3) == [1, 2, 3])
assert(extract([1, 2, 3, 4, 4], None, 4) == [1, 2, 3, 4, 4])

# hi is None
assert(extract([1, 2, 3, 4, 4], 3, None) == [3, 4, 4])
assert(extract([1, 2, 3, 4, 4], 4, None) == [4, 4])

# hi and lo are None
assert(extract([1, 2, 3, 4, 4], None, None) == [1, 2, 3, 4, 4])

# range in first half
assert(extract([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 4) == [2, 3, 4])
assert(extract([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 4) == [1, 2, 3, 4])

# mid range
assert(extract([1, 2, 3, 4, 5], 2, 4) == [2, 3, 4])

# range in second half
assert(extract([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 8) == [6, 7, 8])
assert(extract([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 9) == [6, 7, 8, 9])

# repeated elements
assert(extract([1, 2, 2, 3, 4, 4, 5,], 2, 4) == [2, 2, 3, 4, 4])

# lo and high are equal
assert(extract([1, 2, 2, 3, 4, 4, 5,], 2, 2) == [2, 2])
assert(extract([1, 2, 2, 3, 4, 4, 5,], 4, 4) == [4, 4])
assert(extract([1, 2, 3, 4, 5,], 2, 2) == [2])

# lo lower than minimum value
assert(extract([4, 5, 6, 7, 8, 9], 2, 8) == [4, 5, 6, 7, 8])

# hi higher than maximum value
assert(extract([1, 2, 3, 4, 5, 6], 3, 8) == [3, 4, 5, 6])

#both hi and lo are outside list's range
assert(extract([2, 3, 4, 5, 6], 1, 8) == [2, 3, 4, 5, 6])

#both hi and lo are less than range of list
assert(extract([2, 3, 4, 5, 6], 0, 1) == [])

#both hi and lo are more than range of list
assert(extract([2, 3, 4, 5, 6], 8, 9) == [])

#list of all duplicate values outer range
assert(extract([9, 9, 9, 9, 9, 9], 8, 10) == [9, 9, 9, 9, 9, 9])

#list of all duplicate values range of 9
assert(extract([9, 9, 9, 9, 9, 9], 9, 9) == [9, 9, 9, 9, 9, 9])

# empty list if not in range
assert(extract([9, 9, 9, 9, 9, 9], 8, 8) == [])
