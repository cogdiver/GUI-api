from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base


class cards_table(Base):
    __tablename__ = "cards"

    id = Column(String, primary_key=True)
    process_id = Column(String, ForeignKey("processes.id", ondelete="CASCADE"))
    name = Column(String)
    state = Column(String)
