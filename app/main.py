# General import go here
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

# Specific imports of our Data Models go here:
# Here is the catch: The root directory is /fastapi_pandas$ and that is
# where the DOCKER will run, so the directory of this application MUST
# be included or the container will crash
from app.models import Gender, Role, User, UserUpdateRequest

# Keep the main - call simple
app = FastAPI()

# Create a datastructure which is:
#   ... a type of List and Contains
#   ... Objects of Type User which are
#   ... described in the models.py
#   ... the UUID is given by default for testing resons only
db: List[User] = [
    User(id=UUID("b59c76c4-e7e6-42ae-b411-a7a945e885d8"), first_name="Kevin",
         last_name="Ostheimer", gender=Gender.male, roles=[Role.student]),
    User(id=UUID("a567623c-e70d-4cbd-b42c-cea2bbbe5b6c"), first_name="Alex", last_name="Jones",
         gender=Gender.male, roles=[Role.admin, Role.user])

]

# The design of a modern REST-API endpoint concludes that all
# ... data are transferred in the body. We must not use url parameters
# ... because data security

# HTTP - GET (landing page)


@app.get("/")
async def root():
    return {"hello": "world"}

# HTTP - GET (this is the API endpoint)


@app.get("/api/v1/users")
async def fetch_users():
    return db

# HPPT - POST (this is the API endpoint)


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

# HTTP - DELETE (this is the API endpoint)


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id:{user_id} does not exist")

# HTTP - PUT (this is the API endpoint)


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
