#Lambda Expressions, Map and Filter
#Map built-in funcion
def func(x):
    return x**2
x = [1,2,3,4,5]
for i in map(func, x):
    print(i)
#another way to get map results in a list
print(list(map(func,x)))
#example
def func1(text):
    if len(text)%2 ==0:
        return 'EVEN'
    else:
        return text[0]
names = ['Andy','Eve','Sally']
print(list(map(func1,names)))
#Filter built-in function
def func2(x):
    return x%2 == 0
x = [1,2,3,4,5,6]
a = list(filter(func2,x))
print(a)
#Lambda Expression
#Examples - Converting a function into a lamba expression
def func3(x): #
    r = x**2  #
    return r  #
###############
#step 1       #
###############
def func3_1(x):
    return x**2
###############
#Step 2       #
###############
def func3_1(x): return x**2
###############
#Step 3       #
###############
lambda x: x**2
func3_1 = lambda x: x**2
print(func3_1(5))
#Example (using the map square function we used above)
x=[1,2,3,4,5,6]
print(list(map(lambda x:x**2,x)))
#Example  (using extracting even numbers with filter)
print(list(filter(lambda x:x%2==0,x)))
#Example
n = ['Andy','Eve','Sally']
print(list(map(lambda x:x[0],n)))
print(list(map(lambda x:x[::-1],n)))
