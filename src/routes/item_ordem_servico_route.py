from fastapi import APIRouter, HTTPException
from typing import List
from models.item_ordem_servico import ItemOrdemServicoIn, ItemOrdemServicoOut
from services import item_ordem_servico_service

router = APIRouter()

@router.get("/", response_model=List[ItemOrdemServicoOut])
def listar():
    return item_ordem_servico_service.list_all()

@router.get("/{item_id}", response_model=ItemOrdemServicoOut)
def obter(item_id: int):
    it = item_ordem_servico_service.get(item_id)
    if not it:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return it

@router.post("/", response_model=ItemOrdemServicoOut, status_code=201)
def criar(payload: ItemOrdemServicoIn):
    return item_ordem_servico_service.create(payload.dict())

@router.put("/{item_id}", response_model=ItemOrdemServicoOut)
def atualizar(item_id: int, payload: ItemOrdemServicoIn):
    updated = item_ordem_servico_service.update(item_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return updated

@router.delete("/{item_id}", status_code=204)
def remover(item_id: int):
    ok = item_ordem_servico_service.delete(item_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None