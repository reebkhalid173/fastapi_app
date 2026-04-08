from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/about")
def about():
    return {"info": "This is structured FastAPI app"}