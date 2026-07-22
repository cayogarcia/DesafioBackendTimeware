from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.domain.models import Cliente
from app.repositories.pedido_repository import PedidoRepository
from app.schemas.schemas import PedidoCreate


class PedidoService:

    def __init__(self, db: Session):
        self.db = db
        self.repo = PedidoRepository(db)

    def criar_pedido(self, pedido_data: PedidoCreate):
        cliente = (
            self.db.query(Cliente)
            .filter(Cliente.id == pedido_data.cliente_id)
            .first()
        )
        if not cliente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente não encontrado para este pedido.",
            )

        if pedido_data.valor_total <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O valor total do pedido deve ser maior que zero.",
            )

        return self.repo.create(pedido_data.model_dump())

    def listar_pedidos(self):
        return self.repo.get_all_orm()