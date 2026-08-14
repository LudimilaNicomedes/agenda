## 📊 Demonstração da Interface

<p align="center">
  <img width="400" height="750" alt="Captura de tela 2026-08-06 114843" src="https://github.com/user-attachments/assets/aaa72dc7-fc17-4e47-8822-eb21f9cbc2af" />
  <img width="400" height="750" alt="Captura de tela 2026-08-06 114852" src="https://github.com/user-attachments/assets/41093d91-6562-410b-a3e7-f6c08760399e" />
  <img width="400" height="750" alt="Captura de tela 2026-08-06 114908" src="https://github.com/user-attachments/assets/480a472c-bfa4-411b-b10e-c146fd272f27" />
  <img width="400" height="750" alt="Captura de tela 2026-08-06 120600" src="https://github.com/user-attachments/assets/6fc727bc-6c18-4a92-a6ce-03335c4ea191" />
</p>

Um sistema completo de agendamento e gerenciamento de clientes desenvolvido com **FastAPI**, 
**SQLAlchemy, **SQLite** e um frontend interativo em **HTML5/CSS3/JavaScript**. O projeto foi estruturado seguindo boas práticas de arquitetura de software,
desacoplamento de rotas, controle de migrações de banco de dados e documentação de requisitos.

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
* **Chart.js:** Biblioteca de gráficos para a renderização do dashboard interativo.

---

## 🎨 Funcionalidades

- [x] **Agendamento de Clientes (`UC03`)**: Formular novos agendamentos vinculando Nome, Telefone, Data/Hora e Serviço executado.
- [x] **Visualização Calendária**: Calendário interativo em tempo real para navegação entre dias e meses.
- [x] **Validação e Tratamento de Erros**: Respostas HTTP apropriadas (ex: `422 Unprocessable Entity`) e alertas para o usuário final.
- [x] **Suporte a CORS**: Integração segura entre o servidor backend e a interface web frontend.
- [x] **Controle de Versão de Banco (Alembic)**: Histórico e execução automatizada de scripts de migração de dados.
- [x] **Dashboard e Análise (UC04):** Visualização interativa do total e da distribuição de agendamentos por serviço em determinado mês e ano, acompanhada por gráfico estilo donut e tratamento para períodos sem dados registrados.

## 📁 Estrutura do Projeto

```text
Agenda/
├── alembic/                # Arquivos e versões de migração do banco de dados
│   └── versions/           # Scripts de evolução do schema (Alembic)
├── backend/
│   ├── docs/               # Documentação funcional (Casos de Uso e Requisitos)
│   ├── models/             # Mapeamento das tabelas (SQLAlchemy Models)
│   ├── routers/            # Endpoints da API agrupados por domínio
│   ├── database.py         # Configuração do Engine do SQLAlchemy
│   ├── dependencies.py     # Injeção de dependência (Gerenciamento de Sessão)
│   └── main.py             # Ponto de entrada da aplicação FastAPI
├── frontend/
│   ├── assets/             # Ícones e recursos visuais
│   ├── CSS/                # Estilos visuais da aplicação
│   ├── JS/                 # Scripts de integração da API e calendário
│   └── agenda.html         # Interface principal do agendamento
├── alembic.ini             # Arquivo de configuração do Alembic
├── banco.db                # Banco de dados SQLite
└── requirements.txt        # Dependências do projeto Python
```


A API estará rodando em: `http://127.0.0.1:8000`  
Documentação Swagger interativa: `http://127.0.0.1:8000/docs`





Este projeto está em constante evolução. Novas funcionalidades serão adicionadas conforme o avanço dos estudos e do desenvolvimento.
