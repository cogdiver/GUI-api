from sqlalchemy import Column, String, JSON
from databases import Base


class actions_table(Base):
    __tablename__ = "actions"

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    params = Column(JSON)
    execution_template = Column(String)
