from fastapi import APIRouter

processes_routes = APIRouter()

@processes_routes.get('/')
def listProcesses():
    return 'listProcesses'
