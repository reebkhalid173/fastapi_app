from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home, user

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# include routers
app.include_router(home.router)
app.include_router(user.router)