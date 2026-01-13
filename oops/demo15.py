class A:
    def __init__(self, a):
        self.a = a

    def __init__(self, b, c):
        self.b = b
        self.c = c

    # def __init__(self, a=None, b=None, c=None):
    def __init__(self, *var):
        self.a = var[0]
        self.b = var[1]
        self.c = var[2]

    # def print_a(self):
    #     print(self.a)
    #     print(self.b)
    #     print(self.c)


a3 = A(5, 10, 15)
print(a3.a, a3.b, a3.c)

a1 = A(5)
print(a1.a, a1.b, a1.c)

a2 = A(10, 15)
print(a2.a, a2.b, a2.c)

A(1,2,3,4,5,6,7,8,9)

