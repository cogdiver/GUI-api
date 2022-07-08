from fastapi import APIRouter

reports_routes = APIRouter()

@reports_routes.get('/')
def listReports():
    return 'listReports'
