from sqlalchemy import Column, ForeignKey, String
from databases import Base


class access_table(Base):
    __tablename__ = "access"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("passwords.id", ondelete="CASCADE"))
    permission_id = Column(String, ForeignKey("permissions.id", ondelete="CASCADE"))
