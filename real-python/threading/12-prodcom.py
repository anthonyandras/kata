import random
import time
import concurrent.futures
import threading

FINISH: str = 'THE END'


class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self._producer_pipeline = []
        self._consumer_pipeline = []
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def set_message(self, message):
        print(f"producing message of {message}")
        self.message = message
        self.producer_lock.acquire()
        self._producer_pipeline.append(message)
        self.consumer_lock.release()

    def get_message(self):
        print(f"consuming message of {self.message}")
        message = self.message
        self.consumer_lock.acquire()
        self._consumer_pipeline.append(message)
        self.producer_lock.release()
        return message


def producer(pipeline: Pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)


def consumer(pipeline: Pipeline):
    message = pipeline.get_message()
    while message is not FINISH:
        time.sleep(random.random())


if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
