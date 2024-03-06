from main import repeat

# A few basic, bad input tests.
assert(repeat(None) is None)
assert(repeat([]) is None)
assert(repeat([1]) is None)

# Some small pattern tests.
assert(repeat([1, 1]) == [1])
assert(repeat([1, 1, 1, 1]) == [1, 1])
assert(repeat([1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1])
assert(repeat([1, 1, 1, 1, 1, 1, 1]) == [1])
assert(repeat(['a'] * 23) == ['a'])

# large same element tests
assert(repeat([1,1,1,1,1,1,1,1,1,1] * 40) == [1,1,1,1,1,1,1,1,1,1] * 20)
assert(repeat([1,1,1,1,1,1,1,1,1] * 51) == [1,1,1,1,1,1,1,1,1] * 17)
assert(repeat(['a'] * 100) == ['a'] * 50)
assert(repeat(['a'] * 101) == ['a'])

# dd and even number lists.
assert(repeat([1, 2, 3] * 2) == [1, 2, 3])
assert(repeat([1, 2, 3] * 3) == [1, 2, 3])
assert(repeat([1, 2, 3] * 4) == [1, 2, 3, 1, 2, 3])
assert(repeat([1, 2, 3] * 7) == [1, 2, 3])

# Even number lists.
assert(repeat([1, 2, 3, 1] * 2) == [1, 2, 3, 1])
assert(repeat([1, 2, 3, 1] * 3) == [1, 2, 3, 1])
assert(repeat([1, 2, 3, 1] * 4) == [1, 2, 3, 1, 1, 2, 3, 1])
assert(repeat([1, 2, 3, 1] * 7) == [1, 2, 3, 1])

# checking with characters.
assert(repeat(['a', 'b', 'c'] * 2) == ['a', 'b', 'c'])
assert(repeat(['a', 'b', 'c'] * 3) == ['a', 'b', 'c'])
assert(repeat(['a', 'b', 'c'] * 8) == ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'])
assert(repeat(['a', 'b', 'c'] * 7) == ['a', 'b', 'c'])

# Some longer patterns here.
assert(repeat(['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 2)
               == ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'])

assert(repeat(['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 3)
               == ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'])

assert(repeat(['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 8)
               == ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a', 
                   'a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a', 
                   'a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a', 
                   'a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'])

assert(repeat(['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 23)
              == ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'])

assert(repeat(['a','b'] * 100000) == (['a','b'] * 50000))

assert(repeat(['a','b'] * 100005) == (['a', 'b'] * 33335))

assert(repeat(['a','b','c','d','e','f','g'] * 1429) == (['a','b','c','d','e','f','g']))

assert(repeat(['a','b','c'] * 300009) == (['a','b', 'c'] * 100003))

assert(repeat([*range(1,17)] * 2) == ([*range(1,17)]))
assert(repeat([*range(1,17)] * 3) == ([*range(1,17)]))
assert(repeat([*range(1,17)] * 4) == ([*range(1,17)] * 2))
assert(repeat([*range(1,17)] * 5) == ([*range(1,17)]))
assert(repeat([*range(1,17)] * 6) == ([*range(1,17)] * 3))
assert(repeat([*range(1,17)] * 7) == ([*range(1,17)]))
assert(repeat([*range(1,17)] * 8) == ([*range(1,17)] * 4))
assert(repeat([*range(1,17)] * 9) == ([*range(1,17)] * 3))

assert(repeat([*range(1,201)] * 13) == ([*range(1,201)]))
assert(repeat([*range(1,202)] * 13) == ([*range(1,202)]))

assert(repeat([*range(1,201)] * 50) == ([*range(1,201)] * 25))
assert(repeat([*range(1,202)] * 50) == ([*range(1,202)] * 25))

assert(repeat([1, 2, 3, 'a', 'a', 'a', 1, 2, 3]) == None)
assert(repeat([1, 2, 3, 1, 2, 3, 'a', 'a', 'a']) == None)
assert(repeat(['a', 'a', 'a', 1, 2, 3, 1, 2, 3]) == None)

# Some 'no repeats' tests
assert(repeat([2, 1, 1, 1, 1, 1, 1, 1]) is None)
assert(repeat([1, 2, 1, 1, 1, 1, 1, 1]) is None)
assert(repeat([1, 1, 2, 1, 1, 1, 1, 1]) is None)
assert(repeat([1, 1, 1, 2, 1, 1, 1, 1]) is None)
assert(repeat([1, 1, 1, 1, 2, 1, 1, 1]) is None)
assert(repeat([1, 1, 1, 1, 1, 2, 1, 1]) is None)
assert(repeat([1, 1, 1, 1, 1, 1, 2, 1]) is None)
assert(repeat([1, 1, 1, 1, 1, 1, 1, 2]) is None)

assert(repeat([1, 1, 1, 1, 1, 1, 1, 1, 2]) is None)
assert(repeat([1, 1, 1, 1, 2, 1, 1, 1, 1]) is None)

assert(repeat(([*range(1,202)] * 13).append(1)) is None)

t1 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 2
t1.append('c')
assert(repeat([t1]) is None)


t2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 3
t2.append('c')
assert(repeat([t2]) is None)

t3 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 8
t3.append('c')
assert(repeat([t3]) is None)

t4 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 17
t4.append('c')
assert(repeat([t4]) is None)

t11 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 2
t11.insert(5, 'c')
assert(repeat([t11]) is None)

t12 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 3
t12.insert(5, 'c')
assert(repeat([t12]) is None)


t13 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 6
t13.insert(5, 'c')
assert(repeat([t13]) is None)

t14 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'c', 'a'] * 23
t14.insert(25, 'c')
assert(repeat([t14]) is None)