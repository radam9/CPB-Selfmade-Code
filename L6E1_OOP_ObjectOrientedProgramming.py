#Object Oriented Programming (OOP)
#Class Keywords and Attributes
#Creating a class
class Sample():
    pass

mysample = Sample()
print(type(mysample))

#Step 2 Create attributes
class Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed

mydog = Dog(breed='Lab')
print(type(mydog))
print(mydog.breed)

#Step 3 create more attributes
class Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
mydog = Dog(breed='Lab',name='Sammy',spots=False)
print(mydog.spots)
print(mydog.breed)
print(mydog.name)
