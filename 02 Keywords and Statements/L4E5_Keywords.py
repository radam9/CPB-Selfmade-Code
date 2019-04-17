#break, continue and pass keywords
x = [1,2,3]
for i in x:
    pass #is used when you syntactically need a statement but you dont want any code to be executed
print('script')
mys = 'Sammy'
for l in mys:
    if l == 'a':
        continue #skips the code in the current iteration and goes to the next one in the loop/function
    print(l)
x = 0
while x<5:
    if x == 2:
        break #unlike continue, break completly ends the loop/function
    print(x)
    x += 1
