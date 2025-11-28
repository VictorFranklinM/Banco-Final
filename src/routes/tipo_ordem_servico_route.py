from fastapi import APIRouter, HTTPException
from typing import List
from models.tipo_ordem_servico import TipoOrdemServicoIn, TipoOrdemServicoOut
from services import tipo_ordem_servico_service

router = APIRouter()

@router.get("/", response_model=List[TipoOrdemServicoOut])
def listar():
    return tipo_ordem_servico_service.list_all()

@router.get("/{tipo_id}", response_model=TipoOrdemServicoOut)
def obter(tipo_id: int):
    t = tipo_ordem_servico_service.get(tipo_id)
    if not t:
        raise HTTPException(status_code=404, detail="Tipo de OS não encontrado")
    return t

@router.post("/", response_model=TipoOrdemServicoOut, status_code=201)
def criar(payload: TipoOrdemServicoIn):
    return tipo_ordem_servico_service.create(payload.dict())

@router.put("/{tipo_id}", response_model=TipoOrdemServicoOut)
def atualizar(tipo_id: int, payload: TipoOrdemServicoIn):
    updated = tipo_ordem_servico_service.update(tipo_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Tipo de OS não encontrado")
    return updated

@router.delete("/{tipo_id}", status_code=204)
def remover(tipo_id: int):
    ok = tipo_ordem_servico_service.delete(tipo_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None