# Python
from typing import List

# pydantic
from pydantic import BaseModel

# Utils
from schemas.generals import OwnBaseModel
from models.generals import State

class ProductResponse(OwnBaseModel):
    id: str
    name: str
    image_url: str
    description: str
