class UsageTracker:
    def __init__(self):
        self.calls = 0

    def increment(self):
        self.calls += 1

    def exceeded(self, limit):
        return self.calls > limit
