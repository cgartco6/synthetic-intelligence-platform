from fastapi import APIRouter

router = APIRouter()

AGENTS = [
    {
        "id": "startup_builder",
        "name": "Startup Builder Agent",
        "price": 199,
        "plan": "builder"
    },
    {
        "id": "marketing",
        "name": "Marketing Automation Agent",
        "price": 149,
        "plan": "builder"
    },
    {
        "id": "course_creator",
        "name": "Course Creator Agent",
        "price": 299,
        "plan": "enterprise"
    }
]

@router.get("/marketplace/agents")
def list_agents():
    return AGENTS
