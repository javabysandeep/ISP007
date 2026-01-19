class Arithmetic:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def add(*args):
        sum = 0
        for arg in args:
            sum += arg
        return arg


print(Arithmetic.add(1, 2))
print(Arithmetic.add(1, 2))
print(Arithmetic.add(1, 2))
print(Arithmetic.add(1, 2, 3))
