a=1
b=2
c=3
def f():
    a = 11
    b = 22
    c = 33
    print('local variable a:',a) # 11
    print('local variable b:',b) # 22
    print('local variable c:',c) # 33

    print('global variable a:',globals()['a']) #1
    print('global variable b:',globals()['b']) #2
    print('global variable c:',globals()['c']) #3

f()