from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from backend.models.agenda import Agendamento
from backend.dependencies import pegar_sessao


agenda = APIRouter(prefix="/agendar", tags=["Agendamento"])

class AgendamentosSchema(BaseModel):
    nome: str
    telefone: str
    data_hora: datetime
    servico: str
    

@agenda.post('/agendar')
async def agendamento(dados: AgendamentosSchema, session = Depends(pegar_sessao)):
    novo_agendamento = Agendamento(**dados.model_dump())
    session.add(novo_agendamento)
    session.commit()
    return{"mensagem": "cliente cadastrado com sucesso"}