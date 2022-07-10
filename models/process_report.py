from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databases import Base


class process_report_table(Base):
    __tablename__ = "process_report"

    id = Column(String, primary_key=True)
    process_id = Column(String, ForeignKey("processes.id", ondelete="CASCADE"))
    report_id = Column(String, ForeignKey("reports.id", ondelete="CASCADE"))
