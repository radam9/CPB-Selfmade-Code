#Solution to the Functions and Methods Homework
#Question 1
import math
def vol(rad):
    return (4/3)* math.pi *(rad**3)
print(vol(2))
#Question 2
def ran_check(n,l,h):
    if l<=n<=h:
        return f'{n} is in the range between {l} and {h}'
    else:
        return f'{n} is not in the range between {l} and {h}'
print(ran_check(5,2,7))
#
def ran_bool(n,l,h):
    return l<=n<=h
print(ran_bool(0,1,10))
#Question 3
def up_low(s):
    print(f'Original String : {s}')
    u =[]
    l =[]
    for i in s:
        if i.isupper():
            u.append(i)
        elif i.islower():
            l.append(i)
    print(f'No. of Upper case characters : {len(u)}')
    print(f'No. of Lower case characters : {len(l)}')
text = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(text))
#Question 4
def unique_list(lst):
    return list(set(lst))
x = [1,1,1,1,2,2,3,3,3,3,4,5]
print(unique_list(x))
#Question 5
def multiply(x):
    a = 1
    for i in x:
        a *= i
    return a
print(multiply([1,2,3,-4]))
#Question 6
def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]
print(palindrome('helleh'))
#Question 7
import string
def ispangram(s):
    return len(set(s.lower()) & set(string.ascii_lowercase)) == 26
x = 'The quick brown fox jumps over the lazy dog'
print(ispangram(x))
#Another answer from the solutions
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    # "<=" checks if alphaset is a "subset" of set(str1.lower())
    return alphaset <= set(str1.lower())
x = 'The quick brown fox jumps over the lazy dog'
print(ispangram(x))
