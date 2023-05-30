import threading

num = 0


def add():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num += 1
    lock.release()


def sub():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num -= 1
    lock.release()

if __name__ == "__main__":
    lock = threading.Lock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)