from sqlalchemy import Column, String, ARRAY
from databases import Base


class products_table(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    name = Column(String)
    image_url = Column(String)
    description = Column(String)
