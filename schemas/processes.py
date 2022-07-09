# Python
from typing import List
from datetime import datetime

# pydantic
from pydantic import BaseModel

# Utils
from schemas.generals import OwnBaseModel


class ProcessResponse(OwnBaseModel):
    id: str
    name: str
    description: str
    report_ids: List[str]

class CardResponse(OwnBaseModel):
    id: str
    process_id: str
    state: str
    name: str

class CardDetailsResponse(OwnBaseModel):
    id: str
    path: str
    type_document: str
    entity_name: str
    company_name: str
    range_date: str

class LogResponse(OwnBaseModel):
    id: str
    allow_change: bool
    user_id: str
    time: datetime
    content: str
