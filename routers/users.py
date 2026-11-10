
from fastapi import APIRouter, HTTPException, status

from schemas.user import (
    UserCreate,
    UserUpdate,
    UserPatch,
    UserResponse,
    UserListResponse
)

router = APIRouter()


# Temporary storage
users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Mary", "email": "mary@example.com"},
    {"id": 3, "name": "David", "email": "david@example.com"}
]


# GET: Retrieve all users
@router.get("/", response_model=UserListResponse)
def get_users():
    return {
        "users": users
    }


# GET: Retrieve one user
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# POST: Create a new user
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
def create_user(user_data: UserCreate):

    new_user = {
        "id": max(user["id"] for user in users) + 1,
        "name": user_data.name,
        "email": user_data.email
    }

    users.append(new_user)

    return new_user


# PUT: Replace an existing user's details
@router.put("/{user_id}", response_model=UserResponse)
def replace_user(user_id: int, user_data: UserUpdate):

    for user in users:
        if user["id"] == user_id:

            user["name"] = user_data.name
            user["email"] = user_data.email

            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# PATCH: Update selected user fields
@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserPatch):

    for user in users:
        if user["id"] == user_id:

            updates = user_data.model_dump(exclude_unset=True)

            if not updates:
                raise HTTPException(
                    status_code=400,
                    detail="Provide at least one field to update"
                )

            for field, value in updates.items():

                if value is None:
                    raise HTTPException(
                        status_code=422,
                        detail=f"{field} cannot be null"
                    )

                user[field] = value

            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# DELETE: Remove an existing user
@router.delete("/{user_id}")
def delete_user(user_id: int):

    for user in users:
        if user["id"] == user_id:

            users.remove(user)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
