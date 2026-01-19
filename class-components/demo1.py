class Student:
    # variables
    # methods
    # constructors
    # destructors

    # constructor - initialize an object
    def __init__(self, name, age):
        # assigning local variable value to instance variable
        self.name = name
        self.age = age


ref1 = Student('Amar', 24)
ref2 = Student('Sahil', 24)
ref3 = Student('Swagat', 24)
ref4 = Student('Shubham', 21)
ref5 = Student('Hanumant', 22)
ref6 = Student('Madhavi', 20)
ref7 = Student('Aryan', 23)
ref8 = Student('Bhakti', 16)

print(ref1)#<__main__.Student object at 0x0000026048BF4590>
print(ref1.name) #Amar
print(ref1.age) # 24
