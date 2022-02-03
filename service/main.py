
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest


app = FastAPI()

db: List[User] = [
    User(id=UUID("b59c76c4-e7e6-42ae-b411-a7a945e885d8"), first_name="Jamila",
         last_name="Ahmed", gender=Gender.female, roles=[Role.student]),
    User(id=UUID("a567623c-e70d-4cbd-b42c-cea2bbbe5b6c"), first_name="Alex", last_name="Jones",
         gender=Gender.male, roles=[Role.admin, Role.user])

]


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id:{user_id} does not exist")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):

    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return

    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exist")
