from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Synthetic Intelligence OS")
app.include_router(router)
