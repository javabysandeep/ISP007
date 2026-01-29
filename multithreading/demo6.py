import threading


def m1():
    m2()


def m2():
    m3()


def m3():
    print('m3')


t1=threading.Thread(target=m1)
t2=threading.Thread(target=m1)
t1.start()
t2.start()