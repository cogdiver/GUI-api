# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter, Depends

# Models and schemas
from models.users import *
from models.access import *
from models.actions import *
from models.permissions import *
from models.processes import *
from schemas.users import *

# Utils
from sqlalchemy.orm import Session
from sqlalchemy import and_, any_
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
    path='/{user_id}',
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUsers(user_id, db: Session = Depends(get_db)):
    return db.query(users_table).where(users_table.id == user_id).first()


@users_routes.get(
    path='/{user_id}/permissions',
    response_model=List[UserPermissionsResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUserPermissions(user_id, db: Session = Depends(get_db)):
    return db.query(
        permissions_table
    ).where(
        and_(
            access_table.user_id == user_id,
            access_table.permission_id == permissions_table.id
        )
    ).all()


@users_routes.get(
    path='/{user_id}/processes',
    response_model=List[UserProcessesResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUserProcesses(user_id, db: Session = Depends(get_db)):
    return db.query(
        processes_table
    ).where(
        and_(
            access_table.user_id == user_id,
            access_table.permission_id == permissions_table.id,
            permissions_table.process_id == processes_table.id
        )
    ).all()


@users_routes.get(
    path='/{user_id}/actions',
    # response_model=List[UserActionsResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUserActions(user_id, db: Session = Depends(get_db)):
    return db.query(
        actions_table
    ).where(
        and_(
            access_table.user_id == user_id,
            access_table.permission_id == permissions_table.id,
            actions_table.id == any_(permissions_table.action_ids)
        )
    ).all()
