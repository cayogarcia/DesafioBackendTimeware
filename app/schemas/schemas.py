from datetime import datetime
from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    nome: str
    email: EmailStr


class ClienteCreate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class PedidoBase(BaseModel):
    descricao: str
    valor_total: float


class PedidoCreate(PedidoBase):
    cliente_id: int


class PedidoResponse(PedidoBase):
    id: int
    cliente_id: int
    criado_em: datetime

    class Config:
        from_attributes = True