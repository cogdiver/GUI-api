from pydantic import BaseModel


class OwnBaseModel(BaseModel):
    class Config:
        orm_mode = True
