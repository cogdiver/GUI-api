from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base


class reports_table(Base):
    __tablename__ = "reports"

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    procedure = Column(String)
