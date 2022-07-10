from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from databases import Base
from sqlalchemy import Integer, Enum
from models.generals import State


class permissions_table(Base):
    __tablename__ = "permissions"

    id = Column(String, primary_key=True)
    process_id = Column(String, ForeignKey("processes.id", ondelete="CASCADE"))
    allow_comments = Column(Boolean)
    states = Column(ARRAY(Enum(State)))
