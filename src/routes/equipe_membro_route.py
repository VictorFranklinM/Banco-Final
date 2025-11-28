from fastapi import APIRouter, HTTPException
from typing import List
from models.equipe_membro import EquipeMembroIn, EquipeMembroOut
from services import equipe_membro_service

router = APIRouter()

@router.get("/", response_model=List[EquipeMembroOut])
def listar():
    return equipe_membro_service.list_all()

@router.get("/{membro_id}", response_model=EquipeMembroOut)
def obter(membro_id: int):
    m = equipe_membro_service.get(membro_id)
    if not m:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return m

@router.post("/", response_model=EquipeMembroOut, status_code=201)
def criar(payload: EquipeMembroIn):
    return equipe_membro_service.create(payload.dict())

@router.put("/{membro_id}", response_model=EquipeMembroOut)
def atualizar(membro_id: int, payload: EquipeMembroIn):
    updated = equipe_membro_service.update(membro_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return updated

@router.delete("/{membro_id}", status_code=204)
def remover(membro_id: int):
    ok = equipe_membro_service.delete(membro_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None