
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Mary"},
            {"id": 3, "name": "David"}
        ]
    }


@router.get("/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "John"
    }
