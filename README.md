# 1. Criar venv
## Linux
python -m venv .venv

source .venv/bin/activate
## Windows
.venv\Scripts\activate     

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Subir banco
docker compose up -d
