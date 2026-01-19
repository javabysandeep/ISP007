class Person:
    def __init__(self, name, age):
        #private variables
        self.__name = name
        self.__age = age


p1=Person("Sahil", 18)
#print(p1.name)#AttributeError: 'Person' object has no attribute 'name'
#print(p1.age)#AttributeError: 'Person' object has no attribute 'name'


# this creates new variable called age, it does not modify __age
p1.age=20
print(p1.age)

