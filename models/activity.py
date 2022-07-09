from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATE
from sqlalchemy.orm import relationship
from databases import Base


class activity_table(Base):
    __tablename__ = "activity"

    id = Column(String, primary_key=True)
    card_id = Column(String, ForeignKey("cards.id", ondelete="CASCADE"))
    log_id = Column(String, ForeignKey("logs.id", ondelete="CASCADE"))
