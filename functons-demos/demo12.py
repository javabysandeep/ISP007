x = 1 # global


def f1():
   print(x)
   y=10
   print(y)


def f2():
   print(x)
   #print(y) y is local to f1

def f3():
    x = 44 # local variable

    print(x)


f1()#1
f2()#1
f3()#44