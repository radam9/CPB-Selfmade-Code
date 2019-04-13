#Udemy: Complete Python Bootcamp (Statements Assessment Test)
#Question 1
st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0].lower() == 's':# the lower() is incase there is a capital s somewhere
        print(x)
#Why doesnt this work??
#print([x if x[0] == 's' for x in st.split(' ')])
print([x for x in st.split() if x[0].lower() == 's'])

#Question 2
for x in range(0,11,2):
        print(x)
print([x for x in range(0,11,2)])

#Question 3
x = [i for i in range(1,51) if i % 3 == 0]
print(x)

#Question 4
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x) % 2 == 0:
        print('even!')
print(['even!' for x in st.split() if len(x)%2==0])

#Question 5
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
#Question 6
st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split()])

i = []
for x in st.split():
    i.append(x[0])
print(i)
