from threading import Thread

data = 0

def fun(limit):
    global data
    total=0
    for i in range(limit):
        total+=i
    data = total

thread1 = Thread(target=fun, args=(10_000_000,))
thread1.start()
#thread1.join()
print(data)
