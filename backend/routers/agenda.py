from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from datetime import datetime
from backend.models.agenda import Agendamento
from backend.dependencies import pegar_sessao
from sqlalchemy import extract, func, select



agenda = APIRouter(prefix="/agendar", tags=["Agendamento"])
analise = APIRouter(prefix="/analise", tags=["Analise"])

class AgendamentosSchema(BaseModel):
    nome: str
    telefone: str
    data_hora: datetime
    servico: str
    

@agenda.post('/agendar/')
async def agendamento(dados: AgendamentosSchema, session = Depends(pegar_sessao)):
    novo_agendamento = Agendamento(**dados.model_dump())
    session.add(novo_agendamento)
    session.commit()
    return{"mensagem": "cliente cadastrado com sucesso"}


@analise.get('/dashboard/')
async def dashboard(mes: int = Query(default=None, ge=1, le=12), ano: int = Query(default=None, ge=2000), session = Depends(pegar_sessao)):
    hoje = datetime.now()
    mes_busca = mes if mes is not None else hoje.month
    ano_busca = ano if ano is not None else hoje.year

    hoje = datetime.now()
    mes_busca = mes if mes is not None else hoje.month
    ano_busca = ano if ano is not None else hoje.year

    # Consulta usando a sintaxe moderna select() do SQLAlchemy
    stmt = (
        select(
            Agendamento.servico, 
            func.count(Agendamento.id).label("total")
        )
        .where(
            extract('month', Agendamento.data_hora) == mes_busca,
            extract('year', Agendamento.data_hora) == ano_busca
        )
        .group_by(Agendamento.servico)
    )

    resultados = session.execute(stmt).all()

    if not resultados:
        return {
            "sucesso": False,
            "mensagem": "aviso de dados não encontrados",
            "mes": mes_busca,
            "ano": ano_busca,
            "dados": []
        }

    totais_por_servico = [
        {"servico": servico, "total": total} 
        for servico, total in resultados
    ]
    total_geral = sum(item["total"] for item in totais_por_servico)

    return {
        "sucesso": True,
        "mes": mes_busca,
        "ano": ano_busca,
        "total_agendamentos": total_geral,
        "dados": totais_por_servico
    }