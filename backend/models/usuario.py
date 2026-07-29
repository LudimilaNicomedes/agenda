from backend.database import Base 
from sqlalchemy import Column, String , Integer, Date


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column  ('id', Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=False)
    aniversario = Column ('aniversario', Date, nullable=False)
    telefone = Column('telefone', String, nullable=False )
    senha = Column('senha', String, nullable=False)
    confir_senha = Column('confir_senha', String, nullable=False) 


    def __init__(self, nome, email, aniversario, telefone, senha, confir_senha):
        self.nome = nome
        self.email = email 
        self.aniversario = aniversario
        self.telefone = telefone
        self.senha = senha
        self.confir_senha = confir_senha





    


