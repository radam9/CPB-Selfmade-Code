x = [3,2]
b = []
z = bool()
num = [' ']*10

def func():
    x[1] = x[1] * 2
    z = not z
    num[x[1]] = 'X'
    b.append(x[1])

func()
print(x,'\n',b,'\n',num)
