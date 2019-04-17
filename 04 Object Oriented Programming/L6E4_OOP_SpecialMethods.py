#Object Oriented Programming (OOP)
#Special Methods (Special Methods, Dunder Methods or Magic Methods)
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    #returns back actual string representation so you can print out user defined objects
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book object has been deleted')
b = Book('Python Rocks','Jose',200)
print(b)
len(b)
del b
print(b)

#There are many many more Special/Magic Methods,
#look them up in the documentation, book or tutorial
