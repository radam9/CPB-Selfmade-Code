from random import randint #import randint from random
rn = randint(1,100) #Generate a random intiger between 1 and 100
print('This is a guessing game!\n'+'I will guess a number between 1 and 100 and you have to guess it!')
print('For the first number you guess I will tell you WARM! if its within 10 of the random number')
print('And if it is further away I will tell you that you are COLD!')
print('After that I will tell you WARMER! if you are getting closer to the random number and COLDER! if you are getting further')
print('When you guess the right number I will tell you how many times you have guessed until now')
print('Good Luck, Have Fun and lets start!!!')
a = int(input('Guess a Number: '))
if 0<a<101:
    pass
else:
    print('Your number is out of bounds!')
x = [a]
i=0 #initializing a counter
while x[i] != rn:
    if i <= 0:
        if abs(x[i]-rn) < 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(x[i]-rn) < abs(x[-2]-rn):
            print('WARMER!')
        else:
            print('COLDER!')
    a = int(input('Guess a Number: '))
    if 0<a<101:
        pass
    else:
        print('Your number is out of bounds!')
    i += 1
    x.append(a)
else:
    print( f"{x[-1]} is the right number!\nIt took you {len(x)} tries to guess it.")
