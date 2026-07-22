from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Float, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    pedidos = relationship(
        "Pedido", back_populates="cliente", cascade="all, delete-orphan"
    )


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    descricao = Column(String(255), nullable=False)
    valor_total = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    cliente = relationship("Cliente", back_populates="pedidos")