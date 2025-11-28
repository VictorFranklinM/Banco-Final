# SIGEJ — Sistema de Gestão de Jardinagem e Manutenção
Sistema desenvolvido como trabalho final da disciplina de Banco de Dados 2025.2.

O sistema visa controlar ordens de serviço, equipes e estoque de materiais de
jardinagem e manutenção no IFCE Campus Maracanaú.

---
## Quick Start
```bash
make venv
source .venv/bin/activate
make install
make up
make migrate
make seed
make main
```

Acesse: http://127.0.0.1:8000/docs

## Makefile — Comandos
- **make venv** — cria virtualenv  
- **make install** — instala dependências  
- **make up** — inicia Postgres  
- **make down** — encerra containers  
- **make migrate** — executa 01_create_tables.sql  
- **make seed** — aplica 02_seed.sql  
- **make main** — inicia API FastAPI

---

## Principais Consultas
- `/consultas/ordens-abertas`  
- `/consultas/materiais-criticos`  
- `/consultas/timeline/{os_id}`  
- `/consultas/consumo-equipe?inicio=YYYY-MM-DD&fim=YYYY-MM-DD`  
- `/consultas/os-concluidas/{ano}`  
