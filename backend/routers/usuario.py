from fastapi import APIRouter , Depends, HTTPException, status
from backend.dependencies import pegar_sessao
from backend.models.usuario import Usuario
from backend.main import bcrypt_context
from backend.schemas import UsuarioSchemas
from sqlalchemy.orm import Session


logar = APIRouter(prefix="/login", tags=["Logar"])

criar = APIRouter(prefix="/Criar", tags=["Criar conta"])


@logar.post('/login/')
async def usuario_login(dados: UsuarioSchemas, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == dados.email, Usuario.senha == dados.senha).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha inválidos")
        
    return{'mensagem': 'Login efetuado com sucesso'}



@criar.post('/criar/')
async def usuario_criar(dados: UsuarioSchemas, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == dados.email).first()
    if usuario: 
        return{'erro': 'Este e-mail já está cadastrado'}
    
    usuario = session.query(Usuario).filter(Usuario.telefone == dados.telefone).first()
    if usuario:
        return{'erro': 'Este telefone já está cadastrado'}
    
    
    senha_cripitografada = bcrypt_context.hash(dados.senha)
    novo_usuario = Usuario(dados.nome, dados.email, dados.aniversario, dados.telefone, senha_cripitografada)

    session.add(novo_usuario)
    session.commit()

    return{
        'mensagem': 'Conta criada com sucesso'
    }
