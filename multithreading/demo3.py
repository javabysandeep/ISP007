import threading


def even_print(name):
    for i in range(0, 100, 2):
        print(name, i)


def odd_print(name):
    for i in range(1, 100, 2):
        print(name, i)


even = threading.Thread(target=even_print, args=('even',))
odd = threading.Thread(target=odd_print, args=('odd',))
even.start()
odd.start()

even.join()
odd.join()

print('main thread', threading.current_thread().name)
