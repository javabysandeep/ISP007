# multi level inheritance
class A:
    def display_result(self):
        print("display result")


class B(A):
    def __init__(self):
        print("init B")


class C(B):
    def __init__(self):
        print("init C")


ref = C()
ref.display_result()
