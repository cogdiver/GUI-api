# Utils
from schemas.generals import OwnBaseModel

class ActionResponse(OwnBaseModel):
    id: str
    process_id: str
    name: str
    description: str
    url: str
    params: dict
    execution_template: str
