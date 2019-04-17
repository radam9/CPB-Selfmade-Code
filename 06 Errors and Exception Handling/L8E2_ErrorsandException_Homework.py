#Errors and Error Exceptions Homework
#Question 1
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print('You cannot power a string')
    finally:
        print('If you mean to multiplay the strings here is the result: '+ i*2)
#Question 2
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('You got a Zero Division Error because you tried to divid by Zero')
finally:
    print('All done')
#Question 3
def ask():
    while True:
        try:
            x = int(input('Input an intiger: '))**2
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {x}')
            break

ask()
