from sqlalchemy import Boolean, Column, ForeignKey, String, TIMESTAMP
from databases import Base


class logs_table(Base):
    __tablename__ = "logs"

    id = Column(String, primary_key=True)
    allow_change = Column(Boolean)
    user_id = Column(String, ForeignKey("users.id", ondelete="RESTRICT"))
    time = Column(TIMESTAMP)
    content = Column(String)
