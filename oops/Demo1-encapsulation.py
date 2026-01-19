class Person:
    def __init__(self, name, age):
        #public variables
        self.name = name
        self.age = age


p1=Person("Sahil", 18)
p1.age=-200# since age is public can be accessed directly
print(p1.name)
print(p1.age)# any value can be assigned without any validation

