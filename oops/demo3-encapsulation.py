class Person:
    def __init__(self, name, age):
        # private variables
        self.__name = name
        self.__age = age

    # getter methods to get the value
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # setter methods to set the value
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


p1 = Person("Sahil", 18)
# AttributeError: 'Person' object has no attribute 'name'
# print(p1.name)  # AttributeError: 'Person' object has no attribute 'name'
# print(p1.age)  # AttributeError: 'Person' object has no attribute 'name'
print(p1.get_name())
print(p1.get_age())

# calling setters
p1.set_name("Sahil Z")
p1.set_age(23)

# calling getters
print(p1.get_name())
print(p1.get_age())
