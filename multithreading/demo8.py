# thread execution prevention methods
import threading
import time


def work():
    for i in range(1,100):
       # time.sleep(1)
        print(i)


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)
t1.start()
t2.start()

t1.join(10)
t2.join(10)

print('rest of the main')
