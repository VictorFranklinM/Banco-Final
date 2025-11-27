PYTHON = python
VENV = .venv
VENV_BIN = $(VENV)/bin

DB_SERVICE = postgres
DB_USER = postgres
DB_NAME = sigej
CONTAINER = sigej_postgres

PROJECT_ROOT = $(shell pwd)
SQL_CREATE = $(PROJECT_ROOT)/scripts/01_create_tables.sql
SQL_SEED   = $(PROJECT_ROOT)/scripts/02_seed.sql

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make venv        -> cria virtualenv"
	@echo "  make install     -> instala dependências do requirements.txt"
	@echo "  make up          -> inicia postgres via docker compose"
	@echo "  make down        -> para postgres"
	@echo "  make migrate     -> aplica db/01_create_tables.sql dentro do container"
	@echo "  make seed        -> aplica db/02_seed.sql dentro do container"
	@echo "  make main        -> roda src/main.py"
	@echo ""

venv:
	$(PYTHON) -m venv $(VENV)
	@echo "✔ Ambiente virtual criado (activate: source $(VENV)/bin/activate)."

install:
	$(VENV_BIN)/pip install -r requirements.txt
	@echo "✔ Dependências instaladas."

up:
	docker compose up -d
	@echo "✔ Docker iniciado."

down:
	docker compose down
	@echo "✔ Docker finalizado."

wait-db:
	@echo "Aguardando Postgres ficar pronto no container '$(DB_SERVICE)'..."
	@bash -c '\
		retries=0; \
		until docker compose exec -T $(DB_SERVICE) pg_isready -U $(DB_USER) > /dev/null 2>&1 || [ $$retries -ge 60 ]; do \
			sleep 1; retries=$$((retries+1)); echo -n "."; \
		done; \
		if [ $$retries -ge 60 ]; then echo "\nErro: Postgres não respondeu em 60s"; exit 1; fi; \
		echo "\nPostgres pronto.";'

migrate: wait-db
	@echo "Aplicando migrations (via container) -> $(SQL_CREATE)"
	@cat $(SQL_CREATE) | docker compose exec -T $(DB_SERVICE) psql -U $(DB_USER) -d $(DB_NAME) || ( \
		echo "Piping falhou — tentando fallback com docker cp..."; \
		docker cp $(SQL_CREATE) $(CONTAINER):/tmp/01_create_tables.sql && \
		docker exec -i $(CONTAINER) psql -U $(DB_USER) -d $(DB_NAME) -f /tmp/01_create_tables.sql; \
	)
	@echo "✔ Migrations aplicadas."

seed: wait-db
	@echo "Aplicando seed (via container) -> $(SQL_SEED)"
	@cat $(SQL_SEED) | docker compose exec -T $(DB_SERVICE) psql -U $(DB_USER) -d $(DB_NAME) || ( \
		echo "Piping falhou — tentando fallback com docker cp..."; \
		docker cp $(SQL_SEED) $(CONTAINER):/tmp/02_seed.sql && \
		docker exec -i $(CONTAINER) psql -U $(DB_USER) -d $(DB_NAME) -f /tmp/02_seed.sql; \
	)
	@echo "✔ Seed aplicado."

main:
	$(VENV_BIN)/python src/main.py

.PHONY: help venv install up down wait-db migrate seed migrate-py seed-py main
