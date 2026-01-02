from agents.base_agent import BaseAgent

class HelperAgent(BaseAgent):
    def optimize(self, result):
        optimized = f"Optimized output: {result}"
        self.log(optimized)
        return optimized
