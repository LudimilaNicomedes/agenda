from pydantic import BaseModel
from datetime import date, datetime

class UsuarioSchemas(BaseModel):
    nome: str
    email: str
    aniversario: date
    telefone: str
    senha:str

    class Config:
        from_attributes = True


class AgendamentoSchemas(BaseModel):
    nome: str
    telefone: str
    data_hora: datetime
    servico: str

    class Config:
        from_attributes = True