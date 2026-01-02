from agents.base_agent import BaseAgent

class StrategicAgent(BaseAgent):
    def plan(self, objective):
        plan = f"Strategic plan to achieve: {objective}"
        self.log(plan)
        return plan
