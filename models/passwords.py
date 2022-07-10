from sqlalchemy import Column, ForeignKey, String
from databases import Base


class passwords_table(Base):
    __tablename__ = "passwords"

    id = Column(String, ForeignKey("users.id", ondelete="RESTRICT"), primary_key=True)
    hashed_password = Column(String)
