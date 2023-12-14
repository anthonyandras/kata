class Stack:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, value):
        self._storage.append(value)

    def pop(self):
        if len(self._storage) == 0:
            return None
        return self._storage.pop()
        # Could also do this with try/except blocks
