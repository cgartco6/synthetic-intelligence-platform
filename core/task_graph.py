class TaskNode:
    def __init__(self, description):
        self.description = description
        self.children = []

    def split(self, subtasks):
        for task in subtasks:
            self.children.append(TaskNode(task))
