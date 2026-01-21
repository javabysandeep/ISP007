class Animal:
    def speak(self):
        print("I'm a animal")


class Dog(Animal):
    def speak(self):
        print("I'm a dog")


class Cat(Animal):
    def speak(self):
        print("I'm a cat")


def speak(animal):
    animal.speak()


d = Dog()
c = Cat()

speak(d)
speak(c)
