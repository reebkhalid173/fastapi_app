from fastapi import APIRouter
from app.models.user_model import User

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/{name}")
def get_user(name: str):
    return {"user": name}

@router.post("/")
def create_user(user: User):
    return {
        "message": "User created",
        "data": user
    }