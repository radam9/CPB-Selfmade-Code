#f-string; formatted string literals introduced in python3.6
name = "Jose"
print(f'Hello, his name is {name}')
print(f'Hello, his name is {name!r}')
name = 'Sam'
age = 3
print(f'{name} is {age} years old.')
#float precision: fstring precision refers to total digints not decimals
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
#f-string doesnt add trailing zeroes, so use .format() syntax inside f-fstring
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
print(f"My 10 character, four decimal number is:{num:10.4f}")
