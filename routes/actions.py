from fastapi import APIRouter

actions_routes = APIRouter()

@actions_routes.get('/')
def listActions():
    return 'listActions'
