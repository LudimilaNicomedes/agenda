from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite chamadas de qualquer origem (inclusive a porta 5500)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)



from backend.routers.agenda import agenda
from backend.routers.usuario import logar , criar
app.include_router(agenda)
app.include_router(logar)
app.include_router(criar)