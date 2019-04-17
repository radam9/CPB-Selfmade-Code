#Tuples are similar to lists but they are immutable (unchangable)
t = (1,2,3)
l = [1,2,3]
print(type(t))
print(type(l))
print(len(t))
t2 = ('one',2)
print(t2[0])
print(t2[-1])
#count() method, counts how many times an item shows in a tuple
t = ('a','a','b')
print(t.count('a'))
#index() method, shows the index location of the first time an item appears in tuple
print(t.index('a'))
print(t.index('b'))
