# Python
from typing import List

# pydantic
from pydantic import BaseModel

# Utils
from schemas.generals import OwnBaseModel
from models.generals import State

class UserResponse(OwnBaseModel):
    id: str
    name: str
    email: str

class UserPermissionsResponse(OwnBaseModel):
    id: str
    process_id: str
    allow_comments: bool
    states: List[State]

class UserProcessesResponse(OwnBaseModel):
    id: str
    name: str
    description: str

class UserActionsResponse(OwnBaseModel):
    process_id: str
    id: str
    name: str
    description: str
    url: str
    params: dict
    execution_template: str
