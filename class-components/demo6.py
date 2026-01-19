class Test:
    def __init__(self):
        # static variables
        Test.x = 1
        Test.y = 2
        Test.z = 3

        # instance variables
        self.x = 11
        self.y = 22
        self.z = 33

        # local variables
        x = 111
        y = 222
        z = 333

        print("static variables")
        print(Test.x)
        print(Test.y)
        print(Test.z)
        print("instance variables")
        print(self.x)
        print(self.y)
        print(self.z)
        print("local variables")
        print(x)
        print(y)
        print(z)

ref=Test()
