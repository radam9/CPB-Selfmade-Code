#Nested Statements and Scope
x = 25
def printer():
    x = 50
    return x
print(x)
print(printer())
#LEGB Rule
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
#Examples of Local
lambda x:x**2
#Example of Enclosing Function Locals
#Global
name = 'THIS IS A GLOBAL STRING'
def greet():
    #Enclosing
    name = 'Sammy'
    def hello():
        #Local
        name = 'I am a LOCAL'
        print('Hello '+name)
    hello()
greet()
#More about Golabl and Local
x = 50
def func(x):
    print(f'X is {x}')
    #Local Reassignemnt!!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')
print(func(x))
print(x)
#Reassigning a global variable locally
x1 = 50
def func_1():
    global x1 #get the global variable x1
    print(f'X1 is {x1}')
    #Local Reassignemnt!!
    x1 = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X1 TO {x1}')
print(func_1())
print(x1)
#another safer way to do it is as follows
#its easier to debug as its much cleaner and safer
#since you may accidentally reassign a variable
#specially when you are dealing with bigger programs that contain many scripts and files
x2 = 50
def func_2(x2):
    print(f'X2 is {x2}')
    #Local Reassignemnt!!
    x2 = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X2 TO {x2}')
    return x2
print(x2)
x2=func_2(x2)
print(x2)
