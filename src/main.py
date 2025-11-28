from fastapi import FastAPI
from config import settings
from database import init_db_pool, close_db_pool
from routes.pessoa_route import router as pessoa_router
from routes.tipo_funcionario_route import router as tipo_funcionario_router
from routes.setor_route import router as setor_router
from routes.funcionario_route import router as funcionario_router
from routes.tipo_area_campus_route import router as tipo_area_campus_router
from routes.area_campus_route import router as area_campus_router
from routes.equipe_manutencao_route import router as equipe_manutencao_router
from routes.equipe_membro_route import router as equipe_membro_router
from routes.categoria_material_route import router as categoria_material_router
from routes.unidade_medida_route import router as unidade_medida_router
from routes.fornecedor_route import router as fornecedor_router
from routes.marca_route import router as marca_router
from routes.produto_route import router as produto_router
from routes.cor_route import router as cor_router
from routes.tamanho_route import router as tamanho_router
from routes.produto_variacao_route import router as produto_variacao_router
from routes.local_estoque_route import router as local_estoque_router
from routes.estoque_route import router as estoque_router
from routes.tipo_movimento_estoque_route import router as tipo_movimento_estoque_router
from routes.movimento_estoque_route import router as movimento_estoque_router
from routes.tipo_ordem_servico_route import router as tipo_ordem_servico_router
from routes.status_ordem_servico_route import router as status_ordem_servico_router
from routes.ordem_servico_route import router as ordem_servico_router

app = FastAPI(title="SIGEJ API")

@app.on_event("startup")
def startup():
    init_db_pool()

@app.on_event("shutdown")
def shutdown():
    close_db_pool()

app.include_router(pessoa_router, prefix="/api/v1/pessoas", tags=["Pessoas"])
app.include_router(tipo_funcionario_router, prefix="/api/v1/tipofuncionario", tags=["Tipo Funcionario"])
app.include_router(funcionario_router, prefix="/api/v1/funcionario", tags=["Funcionario"])
app.include_router(setor_router, prefix="/api/v1/setor", tags=["Setor"])
app.include_router(tipo_area_campus_router, prefix="/api/v1/tipoareacampus", tags=["Tipo Area Campus"])
app.include_router(area_campus_router, prefix="/api/v1/areacampus", tags=["Area Campus"])
app.include_router(equipe_manutencao_router, prefix="/api/v1/equipemanutencao", tags=["Equipe Manutencao"])
app.include_router(equipe_membro_router, prefix="/api/v1/equipemembro", tags=["Equipe Membro"])
app.include_router(categoria_material_router, prefix="/api/v1/categoriamaterial", tags=["Categoria Material"])
app.include_router(unidade_medida_router, prefix="/api/v1/unidademedida", tags=["Unidade Medida"])
app.include_router(fornecedor_router, prefix="/api/v1/fornecedor", tags=["Fornecedor"])
app.include_router(marca_router, prefix="/api/v1/marca", tags=["Marca"])
app.include_router(cor_router, prefix="/api/v1/cor", tags=["Cor"])
app.include_router(tamanho_router, prefix="/api/v1/tamanho", tags=["Tamanho"])
app.include_router(produto_router, prefix="/api/v1/produto", tags=["Produto"])
app.include_router(produto_variacao_router, prefix="/api/v1/produtovariacao", tags=["Produto Variacao"])
app.include_router(local_estoque_router, prefix="/api/v1/localestoque", tags=["Local Estoque"])
app.include_router(tipo_movimento_estoque_router, prefix="/api/v1/tipomovimentoestoque", tags=["Tipo Movimento Estoque"])
app.include_router(movimento_estoque_router, prefix="/api/v1/movimentoestoque", tags=["Movimento Estoque"])
app.include_router(estoque_router, prefix="/api/v1/estoque", tags=["Estoque"])
app.include_router(tipo_ordem_servico_router, prefix="/api/v1/tipoordemservico", tags=["Tipo Ordem Servico"])
app.include_router(status_ordem_servico_router, prefix="/api/v1/statusordemservico", tags=["Status Ordem Servico"])
app.include_router(ordem_servico_router, prefix="/api/v1/ordemservico", tags=["Ordem Servico"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT, reload=False)