from agents.strategic_agent import StrategicAgent
from agents.deep_agent import DeepAgent
from agents.ai_agent import AIAgent
from agents.helper_agent import HelperAgent
from core.evaluator import Evaluator

self.evaluator = Evaluator()

score = self.evaluator.score(result)
if score < 7:
    result = self.evaluator.improve(result)

class Orchestrator:
    def __init__(self, memory):
        self.memory = memory
        self.strategic = StrategicAgent(memory)
        self.deep = DeepAgent(memory)
        self.executor = AIAgent(memory)
        self.helper = HelperAgent(memory)

    def run(self, objective: str):
        strategy = self.strategic.plan(objective)
        analysis = self.deep.reason(strategy)
        result = self.executor.execute(analysis)
        support = self.helper.optimize(result)

        return {
            "strategy": strategy,
            "analysis": analysis,
            "result": result,
            "optimized": support
      }
