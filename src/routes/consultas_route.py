from fastapi import APIRouter
from services.consultas_service import consultas_service

router = APIRouter()

@router.get("/ordens-abertas")
def listar_ordens_abertas():
    return consultas_service.listar_ordens_abertas()

@router.get("/materiais-criticos")
def listar_materiais_criticos():
    return consultas_service.listar_materiais_criticos()

@router.get("/timeline/{os_id}")
def listar_timeline_os(os_id: int):
    return consultas_service.listar_timeline_os(os_id)

@router.get("/consumo-equipe")
def listar_consumo_por_equipe(data_inicio: str, data_fim: str):
    """
    Exemplo:
    /consultas/consumo-equipe?data_inicio=2025-10-01&data_fim=2025-10-31
    """
    return consultas_service.listar_consumo_por_equipe(data_inicio, data_fim)

@router.get("/os-concluidas/{ano}")
def listar_os_concluidas_por_tipo(ano: int):
    return consultas_service.listar_os_concluidas_por_tipo(ano)
