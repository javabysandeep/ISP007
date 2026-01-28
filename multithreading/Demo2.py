# creating a thread means assigning worker to do some work
import threading

def task1():
    print('Task1 completed')

def task2():
    print('Task2 completed')

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()  # first thread will be registered with TS
t2.start()  # first thread will be registered with TS
