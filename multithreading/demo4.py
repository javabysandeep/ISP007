import threading

def work():
    for i in range(0, 50, 2):
        print(i)


t1=threading.Thread(target=work)
t1.name='worker' #calling Thread class setter property
t1.start()