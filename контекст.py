class FibonacciIterator:from time import time

class TimerContextManager:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time()
        print(f"Time taken outside the context manager: {self.end_time - self.start_time:.6f} seconds")

with TimerContextManager():
    total = 1
    for i in range(100000):
        total *= (i + 1)