import gc
import time


class Test:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')

t1=Test()
t2=Test()
