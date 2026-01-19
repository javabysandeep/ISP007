# multiple  inheritance
class A:
    def display_result(self):
        print("display result")


class B:
    def __init__(self):
        print("init B")


class C(A, B):
    def __init__(self):
        print("init C")


ref = C()
ref.display_result()
