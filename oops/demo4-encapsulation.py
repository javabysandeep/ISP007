class Person:
    def __init__(self, name, age):
        # private variables
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


p1 = Person("Sahil", 18)
# calling setters
p1.name = "Sahil Z"
p1.age = 23

# calling getters
print(p1.name)
print(p1.age)
