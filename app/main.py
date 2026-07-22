from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Desafio Técnico Backend - Timeware",
    version="1.0.0",
    description="API REST com FastAPI para gestão de Clientes e Pedidos.",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "API rodando com sucesso!"}