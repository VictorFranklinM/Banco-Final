from fastapi import APIRouter, HTTPException
from typing import List
from models.equipe_manutencao import EquipeManutencaoIn, EquipeManutencaoOut
from services import equipe_manutencao_service

router = APIRouter()

@router.get("/", response_model=List[EquipeManutencaoOut])
def listar():
    return equipe_manutencao_service.list_all()

@router.get("/{equipe_id}", response_model=EquipeManutencaoOut)
def obter(equipe_id: int):
    e = equipe_manutencao_service.get(equipe_id)
    if not e:
        raise HTTPException(status_code=404, detail="Equipe não encontrada")
    return e

@router.post("/", response_model=EquipeManutencaoOut, status_code=201)
def criar(payload: EquipeManutencaoIn):
    return equipe_manutencao_service.create(payload.dict())

@router.put("/{equipe_id}", response_model=EquipeManutencaoOut)
def atualizar(equipe_id: int, payload: EquipeManutencaoIn):
    updated = equipe_manutencao_service.update(equipe_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Equipe não encontrada")
    return updated

@router.delete("/{equipe_id}", status_code=204)
def remover(equipe_id: int):
    ok = equipe_manutencao_service.delete(equipe_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None