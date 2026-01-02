from fastapi import FastAPI
from core.synthetic_intelligence import SyntheticIntelligence

app = FastAPI()
si = SyntheticIntelligence()

@app.post("/create")
def create(objective: str):
    return si.think(objective)
