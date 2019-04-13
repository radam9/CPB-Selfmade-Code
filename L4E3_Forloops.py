#For Loops
l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    print(num)
for x in l:
    print('Hello')
#example
for num in l:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')
#example
l_sum = 0
for num in l:
    l_sum = l_sum + num
print(l_sum)
#example with strings
s = 'Hello World'
for letter in s:
    print(letter)
#
for x1 in 'Hello World':
    print(x1)
#if you dont want to use the variable x1 in the for loop anyways use an underscore instead
for _ in 'Hello World':
    print('Hi')
#tuples in for loop
l3 = [(1,2),(3,4),(5,6),(7,8)]
print(len(l3))
for x2 in l3:
    print(x2)
for a,b in l3:
    print(a,'and',b)
    print(a,'only')
l4 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in l4:
    print(a, 'and', c)
#for loops and dictionaries, by default it prints the keys
d = {'k1':1,'k2':2,'k3':3}
for x in d:
    print(x)
#printing dictionary pairs
for x in d.items():
    print(x)
#printing dictionary values
for x in d.values():
    print(x)
#we can also use the same convention as in tuples
for k,v in d.items():
    print('key is:', k)
    print('value is:', v)
#why doesnt this work? , instead of k1,k2,k3 i get k,k,k
for k,v in d:
    print('key is:', k)
    print('value is:', v)
