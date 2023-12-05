import random
import time
import concurrent.futures
import threading
import queue


class Pipeline(queue.Queue):
    def __init__(self, capacity):
        super().__init__(maxsize=capacity)

    def set_message(self, message):
        print(f"producing message of {message}")
        self.put(message)

    def get_message(self):
        message = self.get()
        print(f"consuming message of {message}")
        return message


def producer(pipeline: Pipeline, event: threading.Event):
    while not event.is_set():
        message = random.randint(1, 100)
        pipeline.set_message(message)


def consumer(pipeline: Pipeline, event:  threading.Event):
    while not pipeline.empty() or not event.is_set():
        print(f"queue size is {pipeline.qsize()}")
        message = pipeline.get_message()


if __name__ == '__main__':
    pipeline = Pipeline(10)
    event = threading.Event()   # .set(), .clear()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
