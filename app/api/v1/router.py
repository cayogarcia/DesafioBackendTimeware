from fastapi import APIRouter
from app.api.v1.endpoints import clientes, pedidos

api_router = APIRouter()

api_router.include_router(clientes.router)
api_router.include_router(pedidos.router)