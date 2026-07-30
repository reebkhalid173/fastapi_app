from fastapi import APIRouter
from app.models.user_model import User

router = APIRouter(prefix="/user", tags=["User"])

# In-memory store for demo purposes
fake_db: list[dict] = []


@router.get("/")
def list_users():
    return {"users": fake_db}


@router.get("/{name}")
def get_user(name: str):
    matches = [u for u in fake_db if u["name"].lower() == name.lower()]
    if matches:
        return {"user": matches[0]}
    return {"user": name, "note": "Not found in store — returning name only"}


@router.post("/")
def create_user(user: User):
    fake_db.append(user.model_dump())
    return {
        "message": "User created successfully",
        "data": user
    }