import sys


class Xyz:
    def __init__(self):
        print('Xyz')


t1=Xyz()
t2=Xyz()
t3=Xyz()
print(sys.getrefcount(t1))