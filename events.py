
class Events:
    def __init__(self):
        self._events = {}

    def on(self, event, callback):
        self.events[event] = callback

    def emit(self, event, *args):
        if event in self.events:
            self.events[event](*args)
            return True
        return False