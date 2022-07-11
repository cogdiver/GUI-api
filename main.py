# Fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from routes.users import users_routes
from routes.permissions import permissions_routes
from routes.actions import actions_routes
from routes.reports import reports_routes
from routes.processes import processes_routes
from routes.products import products_routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_routes, prefix='/users', tags=["users"])
app.include_router(permissions_routes, prefix='/permissions', tags=["permissions"])
app.include_router(actions_routes, prefix='/actions', tags=["actions"])
app.include_router(reports_routes, prefix='/reports', tags=["reports"])
app.include_router(processes_routes, prefix='/processes', tags=["processes"])
app.include_router(products_routes, prefix='/products', tags=["products"])

@app.get("/")
async def root():
    return {"message": "Hello root"}
