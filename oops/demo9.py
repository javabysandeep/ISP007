class Outer:
    def __init__(self):
        print('Outer')
    class Inner:
        def __init__(self):
            print('Inner')


outer_ref = Outer()
inner_ref = outer_ref.Inner()

