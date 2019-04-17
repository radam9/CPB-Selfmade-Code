#Error and Exception Handling
#try, except and finally
def add(n1,n2):
    print(n1+n2)

add(10,20)
x1 = 10
x2 = input('please provide a number')

add(x1,x2)

#example
try:
    #code you want to try, it may have an error
    result = 10 + 10
except:
    #what will happen if there is an error
    print('hey it looks like you arent adding correctly')
else:
    print('Addition successful')
    print(result)

#Example 2
try:
    f = open('test','r')
    f.write('Write a test line')
except TypeError:#specifying the type of error to catch
    print('There was a TypeError')
except OSError:#specifying the type of error to catch
    print('Hey you have an OS Error')
finally:
    print('I always run')

#Example 3

def func():
    try:
        x = int(input('Please provide a number: '))
    except:
        print('Whoops! That is not a number')
    finally:
        print('End of try/except/finally')
print(func())

#how to loop the function until i get the required result

def func():
    while True:
        try:#
            x = int(input('Please provide a number: '))
        except:#will run if there is an error
            print('Whoops! That is not a number')
            continue
        else:#will run if you get no error
            print('Yes thank you')
            break
        finally:#will always run whether you get an error or not
            print('End of try/except/finally')
            print('I will always run at the end!')
print(func())
