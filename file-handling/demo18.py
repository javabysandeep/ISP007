# pickling and unpickling
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

with open('student-details.txt','wb') as f:
    person1 = Person("Amar", 22)
    print(person1.name, "\t", person1.age)
    pickle.dump(person1, f)
    print('object saved successfully')

with open('student-details.txt', 'rb') as f:
    person = pickle.load(f)
    print('object loaded successfully')
    print(person.name)
    print(person.age)
