from backend.database import Base
from sqlalchemy import Column, String, Integer, Boolean, Float , DateTime, ForeignKey


#Cria classes/tabelas do banco
class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column('id', Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    telefone = Column('telefone', String, nullable=False)
    data_hora = Column('data_hor6a', DateTime, nullable=False)
    servico = Column('servico', String, nullable=False)

    def __int__(self, nome, telefone, data_hora, servico):
        self.nome = nome
        self.telefone = telefone
        self.data_hora = data_hora
        self.servico = servico
