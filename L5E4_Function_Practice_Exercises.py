#Function practice
#Warmup problems
#Lesser of two evens
def func1(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
func1(2,4)
func1(2,5)
#Animal Crackers
def func2(text):
    text = text.lower().split()
    if text[0][0] == text[1][0]:
        return True
    else:
        return False
#func2 can be reduced to the following
def func2_1(text):
    text = text.lower().split()
    return text[0][0] == text[1][0]
func2_1('Levelheaded Llama')
func2_1('Crazy Kangaroo')
#Makes Twenty
def func3(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False
#func3 can be reduced to the following
def func3_1(a,b):
    return a+b==20 or a==20 or b==20
func3_1(5,15)
func3_1(20,10)
func3_1(1,2)
#Level 1 problems
#Old Macdonald
def func4(name):
    if len(name) >= 4:
        return name[0:3].capitalize() + name[3:].capitalize()
    else:
        print('The entered name was less than 4 characters long')
func4('macdonald')
#Master Yoda
def func5(sentence):
    return ' '.join(sentence.split()[::-1])
func5('I am home')
func5('We are ready')
#Almost there
def func6(x):
    return abs(x-100)<=10 or abs(x-200)<=10
func6(104)
func6(150)
func6(191)
#Level 2 problems
#Find 33
def func7(x):
    a = ''.join(map(str, x))
    return '33' in a
#another answer for func7
def func7_1(x):
    for i in range(0,len(x)-1):
        if x[i] == 3 and x[i+1] == 3:#can also be written if x[i:i+2] == [3,3]:
            return True
    return False
func7([1,3,3])
func7([1,3,1,3])
func7([3,1,3])
#Paper Doll
def func8(text):
    x=[]
    for i in text:
        x.append(i*3)
    return ''.join(x)
#another solution without using functions
def func8_1(text):
    rtext = ''
    for i in text:
        rtext += i*3
    return rtext
func8_1('Hello')
func8_1('Mississippi')
#BlackJack
def func9(a,b,c):
    x=[a,b,c]
    for i in x:#check if values are out of bounds
        if i <1 or i > 11:
            print('Input values mus be between 1 and 11')
    if sum(x) <= 21:
        return sum(x)
    else:
        x = [1 if i==11 else i for i in x]
        if sum(x) <= 21:
            return sum(x)
        else:
            return 'Bust!'
#another form for func9
def func9_1(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return 'Bust!'
func9_1(5,6,7)
func9_1(9,9,9)
func9_1(9,9,11)
#Summer of 69
def func10(array):
    if 6 not in array:
        return sum(array)
    else:
        #x = array[:array.index(6)]+array[array.index(9)+1:]
        return sum(array[:array.index(6)]+array[array.index(9)+1:])
#another solution for func10
def func10_1(array):
    tot = 0
    x = True
    for i in array:
        while x:
            if i != 6:
                tot += i
                break
            else:
                x = False
        while not x:
            if i != 9:
                break
            else:
                x = True
                break
    return tot
func10_1([1, 3, 5])
func10_1([4, 5, 6, 7, 8, 9])
func10_1([2, 1, 6, 9, 11])
#Challenging problems
#Spy Game
def func11(x):
    x = [i for i in x if i==0 or i==7]
    a = ''.join(map(str, x))
    return '007' in a
#another solution to func11
def func11_1(x):
    code = [0,0,7,'x']
    for i in x:
        if i == code[0]:
            code.pop(0)   # code.remove(num) also work
    return len(code) == 1
func11_1([1,2,4,0,0,7,5])
func11_1([1,0,2,4,0,5,7])
func11_1([1,7,2,0,4,5,0])
#Count Primes
def func12(x):
    a = [] #prime number store
    for i in range(2,x+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            a.append(i)
    print(a)
    return len(a)
#another solution to func12
def func12_1(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
func12(100)
