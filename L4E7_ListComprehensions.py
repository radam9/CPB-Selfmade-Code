#List comprehensions
#first lets check the beginners way
mys = 'hello'
myl =list() #we can use a shorter way as follows "myl = []"
for l in mys:
    myl.append(l)
print(myl)
#now lets apply list comprehensions
mys = 'Hello'
myl = [l for l in mys]
print(myl)
#example
myl = [x for x in 'word']
print(myl)
#example 2
myl = [num for num in range(0,11)]
print(myl)
#we can perform operation on the first variable name
#getting square numbers
myl = [num**2 for num in range(0,11)]
print(myl)
#adding an if to the statement
myl = [num for num in range(0,11) if num%2==0]
print(myl)
#example - convertin temp from celcius to fahrenheit
c = [0,10,20,34.5]
f = [((9/5)*temp + 32) for temp in c]
print(f)
#the above example is a shorter way to the following
c = [0,10,20,34.5]
f = []
for temp in c:
    f.append(((9/5)*temp + 32))
print(f)
#using a if and else in a List
myl = [x if x%2==0 else 'odd' for x in range(0,11)]
print(myl)
#the above example represents the following
myl = []
for x in range(0,10):
    if x % 2==0:
        myl.append(x)
    else:
        myl.append('odd')
print(myl)
#nested loops
myl = []
for x in [1,2,3]:
    for y in [1,10,100]:
        myl.append(x*y)
print(myl)
#adding the nested loop in a list comprehension
myl = [x*y for x in [1,2,3] for y in [1,10,100]]
print(myl)
