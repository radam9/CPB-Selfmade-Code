#Decorators
#Mainly used for web developement (Flask and Django)
def func():
    return 1
def hello():
    return 'Hello!'
hello
greet = hello
greet
print(greet())
#
def hello(name='Adam'):
    print('The hello() function has been executed!')
    def greet():
        return '\t This is the greet() function inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')
hello()
#greet and welcome's scope is the hello() function
#if you try to call them outside of that function you will get
#an undefined error
welcome()
#assigning a function to a variable using a return statement
def hello(name='Adam'):
    print('The hello() function has been executed!')
    def greet():
        return '\t This is the greet() function inside hello!'
    def welcome():
        return '\t This is welcome() inside hello'
    print('I am going to return a function!')
    if name == 'Adam':
        return greet
    else:
        return welcome
newfunc = hello()
print(newfunc())
# example
def cool():
    def supercool():
        return 'I am very cool!'
    return supercool
func = cool()
print(func)
#example 2
def hello():
    return 'Hi Adam!'
def other(deffunc):
    print('Other code runs here!')
    print(deffunc())
other(hello)
#Decorators (Manual way)
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
# Decorators automatic way
#@new_decorator passes the funtion below it into new_decorator() and returns the
#result, while keeping the function name as is.
@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()
