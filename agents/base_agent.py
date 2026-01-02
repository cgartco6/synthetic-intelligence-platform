class BaseAgent:
    def __init__(self, memory):
        self.memory = memory

    def log(self, data):
        self.memory.save(data)
