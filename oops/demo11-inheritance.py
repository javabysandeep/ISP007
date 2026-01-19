class A:
    def display_sheets(self):
        print("A::display_sheets :: function")


class B(A):
    def display_sheets(self):
        print("B::display new stuff :: function")
        print("B::display new stuff :: function")
        print("B::display new stuff :: function")
        print("B::display new stuff :: function")


ref = B()
ref.display_sheets()
