from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@router.get("/about")
def about():
    return {"info": "This is a structured FastAPI app"}