from sqlalchemy import text
from sqlalchemy.orm import Session
from app.domain.models import Pedido


class PedidoRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, pedido_data: dict) -> Pedido:
        db_pedido = Pedido(**pedido_data)
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido

    def get_all_orm(self):
        """Exemplo de consulta via ORM"""
        return self.db.query(Pedido).all()

    def get_all_raw_sql(self):
        """Exemplo de consulta via SQL Puro (Raw SQL) exigida no desafio"""
        query = text(
            """
            SELECT p.id, p.descricao, p.valor_total, p.cliente_id, p.criado_em, c.nome as cliente_nome 
            FROM pedidos p 
            INNER JOIN clientes c ON p.cliente_id = c.id
        """
        )
        result = self.db.execute(query)
        return result.fetchall()