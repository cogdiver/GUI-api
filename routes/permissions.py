from fastapi import APIRouter

permissions_routes = APIRouter()

@permissions_routes.get('/')
def listPermissions():
    return 'listPermissions'
