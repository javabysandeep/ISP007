class A:
    def display(self):
        print("A::display")


class B(A):
    def display(self):
        print("B::display")


class C(A, B):
    pass


ref = C()
ref.display()
