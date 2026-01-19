class A:
    def display_result(self):
        print("display result")


class B(A):
    def __init__(self):
        print("init B")

b1 = B()
b1.display_result()
