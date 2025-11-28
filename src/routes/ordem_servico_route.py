from fastapi import APIRouter, HTTPException
from typing import List
from models.ordem_servico import OrdemServicoIn, OrdemServicoOut
from services import ordem_servico_service

router = APIRouter()

@router.get("/", response_model=List[OrdemServicoOut])
def listar():
    return ordem_servico_service.list_all()

@router.get("/{os_id}", response_model=OrdemServicoOut)
def obter(os_id: int):
    o = ordem_servico_service.get(os_id)
    if not o:
        raise HTTPException(status_code=404, detail="Ordem de serviço não encontrada")
    return o

@router.post("/", response_model=OrdemServicoOut, status_code=201)
def criar(payload: OrdemServicoIn):
    return ordem_servico_service.create(payload.dict())

@router.put("/{os_id}", response_model=OrdemServicoOut)
def atualizar(os_id: int, payload: OrdemServicoIn):
    updated = ordem_servico_service.update(os_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Ordem de serviço não encontrada")
    return updated

@router.delete("/{os_id}", status_code=204)
def remover(os_id: int):
    ok = ordem_servico_service.delete(os_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None