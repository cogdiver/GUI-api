from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base
 
 
class users_table(Base):
    __tablename__ = "users"
 
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
