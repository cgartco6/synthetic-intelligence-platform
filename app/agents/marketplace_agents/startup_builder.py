from app.agents.strategic_agent import StrategicAgent
from app.agents.deep_agent import DeepAgent
from app.agents.ai_agent import AIAgent

def run(objective, memory):
    strategy = StrategicAgent(memory).plan(objective)
    analysis = DeepAgent(memory).reason(strategy)
    return AIAgent(memory).execute(analysis)
