# Python
from typing import List

# FastAPI
from fastapi import status, APIRouter, Depends

# Models and schemas
from models.users import *
from models.access import *
from models.permissions import *
from models.processes import *
from models.reports import *
from models.process_report import *
from models.cards import *
from models.details import *
from models.activity import *
from models.logs import *
from schemas.users import *
from schemas.processes import *

# Utils
from sqlalchemy.orm import Session
from sqlalchemy import and_
from databases import get_db

processes_routes = APIRouter()

@processes_routes.get(
    path='/',
    response_model=List[ProcessResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listProcesses(db: Session = Depends(get_db)):
    return db.query(processes_table).all()


@processes_routes.get(
    path='/{process_id}',
    response_model=ProcessResponse,
    status_code=status.HTTP_200_OK,
    summary=""
)
def getProcess(process_id, db: Session = Depends(get_db)):
    return db.query(processes_table).where(processes_table.id == process_id).first()


@processes_routes.get(
    path='/{process_id}/reports',
    response_model=List[ReportResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listProcessReports(process_id, db: Session = Depends(get_db)):
    return db.query(
        reports_table
    ).where(
        and_(
            process_report_table.process_id == process_id,
            process_report_table.report_id == reports_table.id
        )
    ).all()


@processes_routes.get(
    path='/{process_id}/cards',
    response_model=List[CardResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listProcessCards(process_id, db: Session = Depends(get_db)):
    return db.query(cards_table).where(cards_table.process_id == process_id).all()


@processes_routes.get(
    path='/{process_id}/cards/{card_id}',
    response_model=CardResponse,
    status_code=status.HTTP_200_OK,
    summary=""
)
def getCard(process_id, card_id, db: Session = Depends(get_db)):
    return db.query(cards_table).where(
        and_(
            cards_table.process_id == process_id,
            cards_table.id == card_id
        )).first()


@processes_routes.get(
    path='/{process_id}/cards/{card_id}/details',
    response_model=CardDetailsResponse,
    status_code=status.HTTP_200_OK,
    summary=""
)
def getCard(process_id, card_id, db: Session = Depends(get_db)):
    return db.query(details_table).where(
        and_(
            cards_table.process_id == process_id,
            details_table.id == card_id
        )).first()


@processes_routes.get(
    path='/{process_id}/cards/{card_id}/logs',
    response_model=List[LogResponse],
    status_code=status.HTTP_200_OK,
    summary=""
)
def listCardLogs(process_id, card_id, db: Session = Depends(get_db)):
    return db.query(logs_table).where(
        and_(
            cards_table.process_id == process_id,
            activity_table.card_id == card_id,
            logs_table.id == activity_table.log_id
        )).all()
