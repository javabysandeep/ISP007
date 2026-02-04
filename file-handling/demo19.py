# pickling and unpickling
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

with open('student-details.txt', 'rb') as f:
    person = pickle.load(f)
    print(person.name)
    print(person.age)
