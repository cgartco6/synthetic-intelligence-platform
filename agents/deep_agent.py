from agents.base_agent import BaseAgent

class DeepAgent(BaseAgent):
    def reason(self, strategy):
        analysis = f"Deep analysis based on strategy: {strategy}"
        self.log(analysis)
        return analysis
