from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from databases import Base


class passwords_table(Base):
    __tablename__ = "passwords"

    id = Column(String, ForeignKey("users.id", ondelete="RESTRICT"), primary_key=True)
    hashed_password = Column(String)
