from sqlalchemy import Column, ForeignKey, String
from databases import Base


class activity_table(Base):
    __tablename__ = "activity"

    id = Column(String, primary_key=True)
    card_id = Column(String, ForeignKey("cards.id", ondelete="CASCADE"))
    log_id = Column(String, ForeignKey("logs.id", ondelete="CASCADE"))
