#Object Oriented Porgramming
#Inheritence
class Animal():

    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print('I am an Animal')
    def eat(self):
        print('I am eating')

class Dog(Animal):
    def __init__(self):
        #Create an instance of Animal class when I create an instance of my Dog class
        Animal.__init__(self)#how is super().__init__(self) related?
        print('Dog Created')
    #Overriting a method from Animal class
    def who_am_i(self):
        print('I am a dog!')
    #Adding a new Method not exisiting in Animal class
    def bark(self):
        print('WOOF!')
mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()

#Polymorphism
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says meow!'

niko = Dog('Niko')
felix = Cat('Felix')

niko.speak()
felix.speak()

#demonstrating Polymorphism
#Both classes (Dog and Cat) share the same method speak()
#But 1 of them is of type Dog while the other is of type Cat
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

#Another Demonstration
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)

#Abstract classes and Inheritence
#an Abstract class is one that is not expected to have an instence of it Created
#but rather serves as a base class
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')
myanimal = Animal('Fred')
#we get the error when we run the line below, because we were not supposed
#to create an Animal using the Animal() class, rather we were expected to
#inherit the properties of Animal to another class and create an Animal
#using the other class
myanimal.speak()

class Dog(Animal):
    def speak(self):
        return self.name+' says woof!'
class Cat(Animal):
    def speak(self):
        return self.name+' says meow!'

niko = Dog('Niko')
emil = Cat('Emil')
niko.speak()
emil.speak()
