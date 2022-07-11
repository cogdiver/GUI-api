from sqlalchemy import Column, String, ForeignKey
from databases import Base


class processes_table(Base):
    __tablename__ = "processes"

    id = Column(String, primary_key=True)
    product_id = Column(String, ForeignKey('product.id', ondelete='CASCADE'))
    name = Column(String)
    description = Column(String)
