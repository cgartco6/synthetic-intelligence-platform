from agents.base_agent import BaseAgent

class AIAgent(BaseAgent):
    def execute(self, analysis):
        execution = f"Executed task using analysis: {analysis}"
        self.log(execution)
        return execution
