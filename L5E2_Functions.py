#Functions
#Example 1
def func1():
    '''
    This function prints Hello.
    '''
    print('Hello')
func1()
#Example 2
def func2(name):
    '''
    take input 'name' and use it in the function
    '''
    print('Hello ' +name)
func2('Adam')
#using return in the function
def add_func(n1,n2):
    return n1+n2
print(add_func(7,10))
#adding a default to a function
def func3(name='Name'):
    print('Hello '+name)
func3()
func3('Adam')
x = func3('Adam')
print(x)
#since the function is not returning anything, we cannot assign the result to a variale
def func4(name='Name'):
    return 'Hello '+name
func4()
#using return in the Functions
def add_func(n1,n2):
    return n1+n2
x = add_func(7,10)
print(x)
#problem 1
#Find out if the word 'dog' is in a string
def dog_check(x):
    if 'dog' in x.lower():#lower() is used to make sure if a capital letter exists it still recognizes it
        return True
    else:
        return False
dog_check('my dog is running')
#This is a better and shorter version of the upper function
#this is because ('dog' in x) is a boolean in itself so no need to make another boolean
def dog_check2(x):
    return 'dog' in x.lower()
dog_check2('my Dog')
#PIG LATIN example
def pg(word):
    fl = word[0]
    #check if first lettter is vowel
    if fl.lower() in 'aeiou':
        pw = word + 'ay'
    else:
        pw = word[1:] + fl + 'ay'
    return pw
pg('apple')
