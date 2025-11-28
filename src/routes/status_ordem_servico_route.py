from fastapi import APIRouter, HTTPException
from typing import List
from models.status_ordem_servico import StatusOrdemServicoIn, StatusOrdemServicoOut
from services import status_ordem_servico_service

router = APIRouter()

@router.get("/", response_model=List[StatusOrdemServicoOut])
def listar():
    return status_ordem_servico_service.list_all()

@router.get("/{status_id}", response_model=StatusOrdemServicoOut)
def obter(status_id: int):
    s = status_ordem_servico_service.get(status_id)
    if not s:
        raise HTTPException(status_code=404, detail="Status não encontrado")
    return s

@router.post("/", response_model=StatusOrdemServicoOut, status_code=201)
def criar(payload: StatusOrdemServicoIn):
    return status_ordem_servico_service.create(payload.dict())

@router.put("/{status_id}", response_model=StatusOrdemServicoOut)
def atualizar(status_id: int, payload: StatusOrdemServicoIn):
    updated = status_ordem_servico_service.update(status_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Status não encontrado")
    return updated

@router.delete("/{status_id}", status_code=204)
def remover(status_id: int):
    ok = status_ordem_servico_service.delete(status_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None