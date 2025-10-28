from fastapi import FastAPI
from app.routes import health_check, problems_routes
import app.database

api = FastAPI()

api.include_router(health_check.router)
api.include_router(problems_routes.router)