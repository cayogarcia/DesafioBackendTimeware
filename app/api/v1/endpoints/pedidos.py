from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schemas import PedidoCreate, PedidoResponse
from app.services.pedido_service import PedidoService

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post(
    "/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED
)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.criar_pedido(pedido)


@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    service = PedidoService(db)
    return service.listar_pedidos()