# General imports
from typing import Optional, List
from uuid import uuid4
from pydantic import BaseModel
from pydantic.types import UUID4
from enum import Enum

# No specific imports here

# Use Enum for type-safety
# The following Enum classes are the input for the data model


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# A data model is described as class and it's a table with
# 6 columns. They're from 'id' ... 'roles'
# We have a data model for an entry in our database (db)


class User(BaseModel):
    id: Optional[UUID4] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

# We also have a data model for updating an entry. The reason
# is that when we update: Everything except the id is Optional
# So the 'id' is delivered by a query string. Here, for convenience
# the gender can also not be altered


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
