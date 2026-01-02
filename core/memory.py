class Memory:
    def __init__(self):
        self.store = []

    def save(self, data):
        self.store.append(data)

    def recall(self):
        return self.store
