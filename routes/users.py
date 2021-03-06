# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter, Depends

# Models and schemas
from models.users import *
from models.access import *
from models.processes import *
from models.products import *
from models.actions import *
from models.permissions import *
from models.permission_action import *
from schemas.users import *
from schemas.products import *
from schemas.processes import *
from schemas.permissions import *
from schemas.actions import *

# Utils
from sqlalchemy.orm import Session
from sqlalchemy import and_, any_, Column
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
    response_model=List[PermissionResponse],
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
    response_model=List[ProcessResponse],
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
    path='/{user_id}/products',
    response_model=List[ProductResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUserProcesses(user_id, db: Session = Depends(get_db)):
    return db.query(
        products_table
    ).where(
        and_(
            access_table.user_id == user_id,
            access_table.permission_id == permissions_table.id,
            permissions_table.process_id == processes_table.id,
            processes_table.product_id == products_table.id
        )
    ).all()


@users_routes.get(
    path='/{user_id}/actions',
    response_model=List[ActionResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listUserActions(user_id, db: Session = Depends(get_db)):
    return db.query(
        permissions_table.process_id,
        actions_table.id,
        actions_table.name,
        actions_table.description,
        actions_table.url,
        actions_table.params,
        actions_table.execution_template
    ).where(
        and_(
            access_table.user_id == user_id,
            access_table.permission_id == permissions_table.id,
            permission_action_table.permission_id == permissions_table.id,
            permission_action_table.action_id == actions_table.id
        )
    ).all()
