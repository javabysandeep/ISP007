variable=0

def f1():
    global variable
    variable= variable + 1
    print(variable)

def f2():
    global variable
    variable= variable + 1
    print(variable)

def f3():
    global variable
    variable= variable + 1
    print(variable)


f1()
f2()
f3()