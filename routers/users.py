
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Temporary storage: our users live in this Python list.
users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Mary", "email": "mary@example.com"},
    {"id": 3, "name": "David", "email": "david@example.com"}
]


# GET: Retrieve all users
@router.get("/")
def get_users():
    return {
        "users": users
    }


# GET: Retrieve one user
@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
