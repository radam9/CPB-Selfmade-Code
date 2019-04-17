#Object Oriented Programming (OOP)
#Class Object Level Attribute
class Dog():
    #Class Object Attribute
    #Same for any instance of a class (i.e. same for any dog)
    species = 'Mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

mydog = Dog(breed='Lab',name='Sam',spots=False)
print(mydog.species)

#Class Methods
class Dog():
    #Class Object Attribute
    #Same for any instance of a class (i.e. same for any dog)
    species = 'Mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    #Methods (Operations/Actions)
    def bark(self,num):
        print(f'WOOF! My name is {self.name} and the number is {num}')

mydog = Dog('Lab','Frankie')
mydog.bark(7)

#Example
class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        #Only self.pi can be written Circle.pi (since pi is a class object attribute)
        #so self.radius cannot be written as Circle.radius (only class object attributes can)
        self.area = radius*radius*self.pi
    def get_circumference(self):
        return self.radius * self.pi * 2

circle1 = Circle()
circle1.radius
circle2 = Circle(30)
circle2.get_circumference()
circle2.area
