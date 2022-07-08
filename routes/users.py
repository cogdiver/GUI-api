# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter, Depends

# Models and schemas
from models.users import *
from models.access import *
from models.permissions import *
from models.processes import *
from schemas.users import *

# Utils
from sqlalchemy.orm import Session
from sqlalchemy import and_
from databases import get_db, engine


users_routes = APIRouter()

@users_routes.get(
    path='/',
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUsers(db: Session = Depends(get_db)):
    return db.query(users_table).all()


@users_routes.get(
    path='/{id}/processes',
    # response_model=List[UserPermissionsResponse],
    # response_model=List[UserAccessResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def getUserPermissions(id, db: Session = Depends(get_db)):
    processes = db.query(
        permissions_table,
        processes_table
    ).where(
        and_(
            access_table.user_id == id,
            access_table.permission_id == permissions_table.id,
            permissions_table.process_id == processes_table.id
        )
    ).all()

    return processes
