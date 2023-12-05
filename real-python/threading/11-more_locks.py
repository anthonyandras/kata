import threading

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
rlock.release()
print(rlock)
print(threading.current_thread())