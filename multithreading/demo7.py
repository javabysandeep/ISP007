# thread execution prevention methods
import threading
import time


def work():
    for i in range(1,100):
        time.sleep(5)
        print(i)


t1 = threading.Thread(target=work)
t1.start()
