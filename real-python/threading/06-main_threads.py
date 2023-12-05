import time
import threading


def myfunc1(name):
    print(f'myfunc1 started with {name}')
    time.sleep(10)
    print('myfunc1 ended')


def myfunc2(name):
    print(f'myfunc2 started with {name}')
    time.sleep(10)
    print('myfunc2 ended')


def myfunc3(name):
    print(f'myfunc3 started with {name}')
    time.sleep(10)
    print('myfunc3 ended')


if __name__ == '__main__':
    print('main started')
    t1 = threading.Thread(target=myfunc1, args=['anthony'])
    t1.start()
    t2 = threading.Thread(target=myfunc2, args=['was'])
    t2.start()
    t3 = threading.Thread(target=myfunc3, args=['here'])
    t3.start()
    t1.join(timeout=5)
    t2.join(timeout=5)
    t3.join(timeout=5)

    print('main ended')
