from fastapi import FastAPI
from app.routes import health_check, problems_routes
app = FastAPI()

app.include_router(health_check.router)
app.include_router(problems_routes.router)