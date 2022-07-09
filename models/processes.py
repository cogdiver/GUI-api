from sqlalchemy import Column, String, ARRAY
from databases import Base


class processes_table(Base):
    __tablename__ = "processes"

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    report_ids = Column(ARRAY(String))
