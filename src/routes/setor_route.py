from fastapi import APIRouter, HTTPException
from typing import List
from models.setor import SetorIn, SetorOut
from services import setor_service

router = APIRouter()

@router.get("/", response_model=List[SetorOut])
def listar():
    return setor_service.list_all()

@router.get("/{setor_id}", response_model=SetorOut)
def obter(setor_id: int):
    s = setor_service.get(setor_id)
    if not s:
        raise HTTPException(status_code=404, detail="Setor não encontrado")
    return s

@router.post("/", response_model=SetorOut, status_code=201)
def criar(payload: SetorIn):
    return setor_service.create(payload.dict())

@router.put("/{setor_id}", response_model=SetorOut)
def atualizar(setor_id: int, payload: SetorIn):
    updated = setor_service.update(setor_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Setor não encontrado")
    return updated

@router.delete("/{setor_id}", status_code=204)
def remover(setor_id: int):
    ok = setor_service.delete(setor_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None