#Files, Input and Output
#use .open() to open a file
myfile = open('test.txt')
#use .read() method to read the contents of the file
print(myfile.read())
#after you read a file the cursor stays at the end of the file.
#so if you .read() again you will get a space.
print(myfile.read())
#to reset the position of the cursor use the .seek() method
myfile.seek(0)
contents = myfile.read()
print(contents)
#use .readlines() method to save each line as a seperate object in the list
#just as the .read() method the cursor needs to be reset after using .readlines()
myfile.seek(0)
print(myfile.readlines())
#opening a file with full path
myfile = open('D:\\Python\\Courses\\[FreeCourseSite.com] Udemy - Complete Python Bootcamp Go from zero to hero in Python 3\\Selfmade python codes\\test.txt')
#you need to close the file after done working for not to get errors
myfile.close()
#to skip worrying about closing a file use the with Keyword
with open('test.txt') as newfile:
    contents = newfile.read()
    print(contents)
#mode sets which state your openning the file in (read only, write only..etc)
with open('newfile.txt',mode='r') as f:
    print(f.read())
#appending text to a file
with open('newfile.txt',mode='a') as f:
    f.write('FOUR ON FORTH')
with open('newfile.txt',mode='r') as f:
    print(f.read())
#creating a new file and writing on it
with open('test2.txt',mode='w') as f:
    f.write('I created this file!')
