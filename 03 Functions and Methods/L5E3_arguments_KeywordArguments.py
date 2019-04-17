#Arguments *args and Keyword Arguments **kwargs
def func(a,b):
    #returns %5 of the sum of a and b
    return sum((a,b)) * 0.05
func(40,60)
# a and b are positional arguments
# 40 was assignemt to a because it was in the first position/argument
# 60 was assignemt to a because it was in the second position/argument
# *args is used to allow the function to take any number of inputs/arguments
# *args allowes the function to take an arbetrary number of arguments
#*args returns a tuple
def func(*args):
    return sum(args) * 0.05
func(40,60,100,987,578,3)
#another example
def func(*args):
    for i in args:
        print(i)
func(1,7,9,633,47)

#**kwargs returns a dictionary
def func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
func(fruit='apple',veggie='lettuce')
#example to use *args and **kwargs in combination
#since *args is first and **kwargs is second, the input in the function has to also be in the same order
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
func(10,20,30,fruit='orange',food='eggs',animal='dog')
