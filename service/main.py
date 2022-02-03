from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User


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
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}
