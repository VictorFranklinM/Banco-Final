from fastapi import FastAPI
from config import settings
from database import init_db_pool, close_db_pool
from routes.pessoa_route import router as pessoa_router
from routes.tipo_funcionario_route import router as tipo_funcionario_router

app = FastAPI(title="SIGEJ API")

@app.on_event("startup")
def startup():
    init_db_pool()

@app.on_event("shutdown")
def shutdown():
    close_db_pool()

app.include_router(pessoa_router, prefix="/api/v1/pessoas", tags=["Pessoas"])
app.include_router(tipo_funcionario_router, prefix="/api/v1/tipofuncionario", tags=["Tipo Funcionario"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT, reload=False)