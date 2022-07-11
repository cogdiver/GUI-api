# Python
from typing import List

# Utils
from schemas.generals import OwnBaseModel
from models.generals import State

class PermissionResponse(OwnBaseModel):
    id: str
    process_id: str
    allow_comments: bool
    states: List[State]
