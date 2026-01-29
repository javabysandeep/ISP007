# race condition : multiple threads updating the shared data ---> wrong result
import threading

counter = 0
threads = []
lock = threading.Lock()


def increment():
    global counter
    for i in range(1000):
        lock.acquire()
        counter += 1


for i in range(1000):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)
