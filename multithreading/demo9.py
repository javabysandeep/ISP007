# thread execution prevention methods
import threading
import time


def work():
    for i in range(1,100):
        time.sleep(10)
        print(i)


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)
t1.start()
t2.start()

print(t1.is_alive())
print(t2.is_alive())
print('rest of the main')
