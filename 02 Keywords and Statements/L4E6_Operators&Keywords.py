#Useful keywords and operators
#range() is a generator
for x in range(10):
    print(x)
for x in range(3,10):
    print(x)
for x in range(0,11,2):
    print(x)
#generat a list using range()
exl = list(range(10))
print(exl)
#enumerate
ic = 0
for l in 'abcde':
    print('At index {} the letter is {}'.format(ic,l))
    ic += 1
word = 'abcde'
for l in enumerate(word):
    print(l)
#or
for i,l in enumerate(word):
    print(i, 'and', l)
#zip , it will combine the lists according to the length of the shortest list
#zip can be used with different iterated objects (string,list,dic...etc)
#and you can combine different kinds together
myl1 = [1,2,3,]
myl2 = 'abc'
for i in zip(myl1,myl2):
    print(i)
#example
myl1 = [1,2,3,4,5]
myl2 = ['a','b','c']
myl3 = [100,200,300]
for i in zip(myl1,myl2,myl3):
    print(i)
#generate a list of tuples
exl2 = list(zip(myl1,myl2))
print(exl2)
#in operator, its in the for loop, but can also be used to check if an object is in list
print('x'in[1,2,3])
print('x'in['x','y','z'])
print('a'in'a world')
print('k'in{'k':345})
d={'k':345}
print(345 in d.values())
#min and max functions
myl = [10,20,30,40,100]
print(min(myl))
print(max(myl))
#python random library
from random import shuffle
myl = [1,2,3,4,5,6,7,8,9,10]
shuffle(myl) #shuffle is an inplace function
print(myl)
shuffle(myl)
print(myl)
#randint for grabbing a random intiger
from random import randint
x = randint(0,1000)
print(x)
#input , to accept a user input (input accepts anything passed into it as a string)
input('enter a number here')
y = input('What is your name? ')
print(y)
#example
x = input('whats your favorite number?: ')
print(type(x))
x = int(x) #we can also use float()
print(type(x))
#or we can do it in one line as follows
x = int(input('Favorite number: '))
print(type(x))
