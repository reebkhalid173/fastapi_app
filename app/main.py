from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home, user
import os

app = FastAPI(title="FastAPI Web App", version="1.0.0")

# Static files — served from app/static/
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

# Routers
app.include_router(home.router)
app.include_router(user.router)