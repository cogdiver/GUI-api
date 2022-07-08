# Python
from typing import List

# Utils
from schemas.generals import OwnBaseModel


class UserResponse(OwnBaseModel):
    id: str
    name: str
    email: str

class UserPermissionsResponse(OwnBaseModel):
    id: str
    process_id: str
    allow_comments: bool
    states: List[str]
    action_ids: List[str]

class UserAccessResponse(OwnBaseModel):
    id: str
    user_id: str
    permission_id: str
