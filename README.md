## 📊 Demonstração da Interface

<p align="center">
 <img width="400" height="700" alt="Captura de tela 2026-08-06 114843" src="https://github.com/user-attachments/assets/a8cf4121-89d2-49fb-a681-93de9b3a2b31" />
 <img width="400" height="700" alt="Captura de tela 2026-08-06 114852" src="https://github.com/user-attachments/assets/e3edaebe-e3da-479b-91a9-ecfb818b1172" />
 <img width="400" height="700" alt="Captura de tela 2026-08-06 114908" src="https://github.com/user-attachments/assets/bd85e972-96e0-4dba-a353-28c494fc95b2" />
 <img width="400" height="700" alt="Captura de tela 2026-08-06 120600" src="https://github.com/user-attachments/assets/f91d6918-340e-41ba-8721-2ff01954b310" />
</p>


# 📅 Agenda

Uma aplicação simples e funcional para gerenciamento de compromissos e tarefas do dia a dia.

**Agenda** foi desenvolvido para ajudar na organização pessoal e de rotina, permitindo registrar, visualizar e gerenciar tarefas de forma prática.


## 🚀 Tecnologias Utilizadas

### **Backend**
* **Python 3.10+**
* **FastAPI**: Framework web moderno, assíncrono e de alta performance.
* **SQLAlchemy 2.0**: ORM para mapeamento objeto-relacional e manipulação do banco de dados.
* **SQLite**: Banco de dados relacional leve para armazenamento de dados.
* **Alembic**: Ferramenta de migração de banco de dados e controle de versão de schemas.
* **Pydantic**: Validação de dados de entrada/saída e schemas de requisição.
* **Uvicorn**: Servidor ASGI de altíssima velocidade.

### **Frontend**
* **HTML5 & CSS3**: Interface responsiva e estilizada com variáveis CSS, tipografia personalizada (Google Fonts) e paleta moderna.
* **JavaScript (ES6+)**: Consumo de API via `fetch` assíncrono e manipulação do DOM.
* **Flatpickr**: Integração de calendário interativo com suporte a localização em Português (`pt-BR`).

---

## 🎨 Funcionalidades

- [x] **Autenticação Segura de Usuários (`UC01`)**: Sistema de login e cadastro com **criptografia de senha (hashing via Bcrypt)** e validação de dados via Pydantic.
- [x] **Agendamento de Clientes (`UC03`)**: Formulação de novos agendamentos vinculando Nome, Telefone, Data/Hora e Serviço executado.
- [x] **Visualização Calendária**: Calendário interativo em tempo real para navegação entre dias e meses.
- [x] **Validação e Tratamento de Erros**: Respostas HTTP apropriadas (ex: `401 Unauthorized`, `422 Unprocessable Entity`) e alertas dinâmicos para o usuário.
- [x] **Suporte a CORS**: Integração segura entre o servidor backend e a interface web frontend.
- [x] **Controle de Versão de Banco (Alembic)**: Histórico e execução automatizada de scripts de migração de dados.

---

## 📁 Estrutura do Projeto

```text
Agenda/
├── alembic/                # Arquivos e versões de migração do banco de dados
│   └── versions/           # Scripts de evolução do schema (Alembic)
├── backend/
│   ├── docs/               # Documentação funcional (Casos de Uso e Requisitos)
│   ├── models/             # Mapeamento das tabelas (SQLAlchemy Models)
│   ├── routers/            # Endpoints da API agrupados por domínio (Login, Cadastro, Agenda)
│   ├── database.py         # Configuração do Engine do SQLAlchemy
│   ├── dependencies.py     # Injeção de dependência (Gerenciamento de Sessão)
│   └── main.py             # Ponto de entrada da aplicação FastAPI

├── frontend/
│   ├── assets/             # Ícones e recursos visuais
│   ├── CSS/                # Estilos visuais da aplicação (usuario.css, agenda.css)
│   ├── JS/                 # Scripts de integração da API, login e calendário
│   ├── agenda.html         # Interface principal do agendamento
│   ├── cadastro.html       # Interface de cadastro de usuários
│   └── login.html          # Interface de autenticação
├── alembic.ini             # Arquivo de configuração do Alembic
├── banco.db                # Banco de dados SQLite
└── requirements.txt        # Dependências do projeto Python



