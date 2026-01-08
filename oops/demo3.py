class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add(self,id):
        self.id = id

s1=Student('Amar',23) # 1. creating instance variables using constructor
s1.add(1) # 2. creating instance variables using method
s1.address = 'Pune' # 3. creating instance variable outside the class

print(s1.id)
print(s1.name)
print(s1.age)
print(s1.address)

