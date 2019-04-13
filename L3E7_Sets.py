#Sets
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
#Sets only carry 1 of each item so if we add 2 again nothing happens to the set
myset.add(2)
print(myset)
#Sets can only carry Numbers and Strings
myset = {1,2,'abc',0.1,-300}
print(myset)
#you can convert a list to a set in the following way
#notice that it only took 1 of each item (1,2 and 3)
klist = [1,1,2,3,4,7,4,1,2,3,3]
myset = set(klist)
print(myset)
