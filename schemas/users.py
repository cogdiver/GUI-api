# Python
from typing import List

# pydantic
from pydantic import BaseModel

# Utils
from schemas.generals import OwnBaseModel

class UserResponse(OwnBaseModel):
    id: str
    name: str
    email: str
