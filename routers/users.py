
from fastapi import APIRouter, HTTPException, status

from schemas.user import UserCreate

router = APIRouter()


# Temporary storage
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


# POST: Create a new user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):

    new_user = {
        "id": max(user["id"] for user in users) + 1,
        "name": user_data.name,
        "email": user_data.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }
