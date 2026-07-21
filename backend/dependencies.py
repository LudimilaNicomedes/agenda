from sqlalchemy.orm import sessionmaker
from backend.database import db

def pegar_sessao():
    try:
        #Cria uma sessao no banco de dados 
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()