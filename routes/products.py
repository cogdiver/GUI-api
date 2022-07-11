# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter, Depends

# Models and schemas
from models.products import *
from schemas.products import *

# Utils
from sqlalchemy.orm import Session
from sqlalchemy import and_, any_, Column
from databases import get_db, engine

products_routes = APIRouter()

@products_routes.get(
    path='/',
    response_model=List[ProductResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listProducts(db: Session = Depends(get_db)):
    return db.query(
        products_table
    ).all()


@products_routes.get(
    path='/{product_id}',
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK,
    summary=""
)
def listProducts(product_id, db: Session = Depends(get_db)):
    return db.query(
        products_table
    ).where(
        products_table.id == product_id
    ).first()