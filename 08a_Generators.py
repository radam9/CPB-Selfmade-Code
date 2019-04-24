#Generators
def cubes(x):
    result = []
    for i in range(x):
        result.append(i**3)
    return result
cubes(10)

def cubes2(x):#this function is similar to range()
    for i in range(x):
        yield i**3

for x in cubes2(10):
    print(x)

list(cubes2(10))
#Example (Fibonachi sequence)
def fib(x):
    a = 1
    b = 1
    for i in range(x):
        yield a
        a,b = b,a+b

for num in fib(10):
    print(num)
#Next function
def func():
    for x in range(3):
        yield x

for x in func():
    print(x)

g = func()
next(g)
#Iter function
s = 'hello'
for i in s:
    print(i)
next(s)
s_iter = iter(s)#convert a string into an iterable object like a generator
next(s_iter)
