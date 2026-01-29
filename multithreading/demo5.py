import threading


def work1():
    for i in range(0, 50, 2):
        print(i)


def work2():
    print(10 / 0)


t1 = threading.Thread(target=work1)
t1.name = 'worker'  # calling Thread class setter property
t2 = threading.Thread(target=work2)


t1.start()
t2.start()


print('rest of the main')