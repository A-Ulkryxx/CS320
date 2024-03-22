from main import placement

# Expected Call Length
assert(len(placement(4, ((True, False, False, True ), 
                          (False, False, True, False ), 
                          (True, True, False, True ) ))) == 4)


# More objects than Available spots
assert(placement(4, ( (True, False, False, False ), 
                      (False, False, True, False ), 
                      (False, False, False, True ) )) == None)


# All False Spots
assert(placement(4, ( (False, False, False, False ), 
                      (False, False, False, False ), 
                      (False, False, False, False ) )) == None)


# Non-Rectangular Map
assert(placement(4, ( (True, False, False, False ), 
                          (False, False, True), 
                          (False, False, False, True ) )) == None)


# One Row
assert(placement(4, ((True, False, False, False ))) == None)


# Map of None
assert(placement(4, None) == None)


# Empty Map
assert(placement(4, ()) == None)

assert(placement(4, (())) == None)


# Non-positive num_objects
assert(placement(0, ((True, False, False, True ), 
                          (False, False, True, False ), 
                          (True, True, False, True ) )) == None)

assert(placement(-1, ((True, False, False, True ), 
                          (False, False, True, False ), 
                          (True, True, False, True ) )) == None)