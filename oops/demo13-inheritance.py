class Parent:
    def __init__(self):
        self._x = 10  # protected
        self.__y = 20  # private
        self.z = 30  # public


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.parent_x = self._x
        self.parent_y = self.z

        self._x = 100  # protected
        self.__y = 200  # private
        self.z = 300  # public

    def display(self):
        print('super class variables')
        print(self.parent_x)
        print(self.parent_y)

        print('child class variables')
        print(self._x)
        print(self.__y)
        print(self.z)


ref = Child()
ref.display()
