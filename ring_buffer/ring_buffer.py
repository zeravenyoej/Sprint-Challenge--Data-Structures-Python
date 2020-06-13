class RingBuffer:
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.store = [None]*capacity
        self.oldest = 0

    def append(self, item):
        self.store[self.oldest] = item
        if self.oldest == self.capacity - 1:
            self.oldest = 0
        else:
            self.oldest += 1

    def get(self):
        return [item for item in self.store if item is not None]

