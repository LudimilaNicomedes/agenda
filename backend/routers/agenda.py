from fastapi import APIRouter, Depends
from backend.models.agenda import Agendamento
from backend.dependencies import pegar_sessao
from backend.schemas import AgendamentoSchemas
from sqlalchemy.orm import Session


agenda = APIRouter(prefix="/agendar", tags=["Agendamento"])


@agenda.post('/agendar/')
async def agendamento(dados: AgendamentoSchemas, session: Session= Depends(pegar_sessao)):
    novo_agendamento = Agendamento(**dados.model_dump())
    session.add(novo_agendamento)
    session.commit()
    return{"mensagem": "cliente cadastrado com sucesso"}


