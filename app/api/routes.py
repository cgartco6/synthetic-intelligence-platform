from fastapi import APIRouter, Depends
from app.core.synthetic_intelligence import SyntheticIntelligence
from app.api.auth import verify_user

router = APIRouter()
si = SyntheticIntelligence()

@router.post("/create")
def create(objective: str, user=Depends(verify_user)):
    return si.think(objective)
