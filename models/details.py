from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base


class details_table(Base):
    __tablename__ = "details"

    id = Column(String, ForeignKey("cards.id", ondelete="CASCADE"), primary_key=True)
    path = Column(String)
    type_document = Column(String)
    entity_name = Column(String)
    company_name = Column(String)
    range_date = Column(String)
