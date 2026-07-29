from fastapi import APIRouter , Depends, HTTPException, status
from backend.dependencies import pegar_sessao
from pydantic import BaseModel
from datetime import date
from backend.models.usuario import Usuario


logar = APIRouter(prefix="/login", tags=["Logar"])

criar = APIRouter(prefix="/Criar", tags=["Criar conta"])

class LoginSchema(BaseModel):
    email: str
    senha: str

class UsuarioSchema(BaseModel):
    nome : str
    email: str
    aniversario: date
    telefone: str
    senha: str
    confir_senha: str

@logar.post('/login/')
async def usuario_login(dados : LoginSchema, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == dados.email, Usuario.senha == dados.senha).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha inválidos")
        
    
    return{'mensagem': 'Login efetuado com sucesso'}



@criar.post('/criar/')
async def usuario_criar(dados : UsuarioSchema, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == dados.email).first()
    if usuario: 
        return{'erro': 'Este e-mail já está cadastrado'}
    
    usuario = session.query(Usuario).filter(Usuario.telefone == dados.telefone).first()
    if usuario:
        return{'erro': 'Este telefone já está cadastrado'}
    
    usuario = session.query(Usuario).filter(Usuario.confir_senha != dados.senha).first()
    if usuario:
        return{'erro': 'Senhas não coincidem'}
    
    novo_usuario = Usuario(dados.nome, dados.email, dados.aniversario, dados.telefone, dados.senha, dados.confir_senha)

    session.add(novo_usuario)
    session.commit()

    return{
        'mensagem': 'Conta criada com sucesso'
    }
