# SARA
Supervisor Autônomo de Rede de Água


---
## Setup
### Implantação da central
#### Windows
```python
cd central
python -m  venv .venv
.\.venv\Scripts\activate

pip install poetry
poetry install

poetry run uvicorn main:app --reload --port 8000
```

#### Adicionar seu .env com suas variáveis de aplicação
```
PROJECT_NAME="Central Local"  
DESCRIPTION="API Central da SARA"  
OPENAPI_PREFIX=""
POSTGRES_SERVER="localhost"
POSTGRES_PORT=5432
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="postgres"
POSTGRES_DB="SARA"
FIRST_SUPERUSER="Admin"
FIRST_SUPERUSER_PASSWORD="Admin"
CLIMATE_API_KEY="Sua Chave da Api do Clima Tempo https://advisor.climatempo.com.br/"
```
