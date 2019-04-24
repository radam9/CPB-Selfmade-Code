#Problem 1
def square(x):
    for i in range(x):
        yield i**2

for x in square(10):
    print(x)

#Problem 2
import random

def gener(l,h,x):
    for _ in range(x):
        yield random.randint(l,h)
for x in gener(1,10,12):
    print(x)

#Problem 3
s = 'Hello'
s_it = iter(s)
print(next(s))

#Credit Problem
#Generator comprehension

list = [1,2,3,4,5]
gencomp = (item for item in list if item > 3)
for item in gencomp:
    print(item)
    
