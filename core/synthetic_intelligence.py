from core.orchestrator import Orchestrator
from core.memory import Memory

class SyntheticIntelligence:
    def __init__(self):
        self.memory = Memory()
        self.orchestrator = Orchestrator(self.memory)

    def think(self, objective: str):
        return self.orchestrator.run(objective)
