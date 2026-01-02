from fastapi import APIRouter

router = APIRouter()

@router.get("/owner/stats")
def stats():
    return {
        "users": 0,
        "monthly_revenue": 0,
        "agent_calls": 0,
        "profit_estimate": "OK"
    }
