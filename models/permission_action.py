from sqlalchemy import Column, ForeignKey, String
from databases import Base


class permission_action_table(Base):
    __tablename__ = "permission_action"

    id = Column(String, primary_key=True)
    permission_id = Column(String, ForeignKey("permissions.id", ondelete="CASCADE"))
    action_id = Column(String, ForeignKey("actions.id", ondelete="CASCADE"))
