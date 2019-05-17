from threading import Lock, Thread
from events import Events



class Workers:
    def __init__(self, max_):
        self.max = max_
        self.events = Events()
        self.queue = []
        self.pool = []
        self.working_count = 0

        for i in range(max_):
            self.pool.append(Thread())

    def add(self, f, *args):
        self.queue.append((f, args))