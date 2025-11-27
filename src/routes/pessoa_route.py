from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.pessoa import PessoaIn, PessoaOut
from services import pessoa_service

router = APIRouter()

@router.get("/", response_model=List[PessoaOut])
def listar_pessoas():
    return pessoa_service.list_pessoas()

@router.get("/{pessoa_id}", response_model=PessoaOut)
def obter_pessoa(pessoa_id: int):
    p = pessoa_service.get_pessoa(pessoa_id)
    if not p:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return p

@router.post("/", response_model=PessoaOut, status_code=201)
def criar_pessoa(payload: PessoaIn):
    created = pessoa_service.create_pessoa(payload.dict())
    return created

@router.put("/{pessoa_id}", response_model=PessoaOut)
def atualizar_pessoa(pessoa_id: int, payload: PessoaIn):
    updated = pessoa_service.update_pessoa(pessoa_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return updated

@router.delete("/{pessoa_id}", status_code=204)
def remover_pessoa(pessoa_id: int):
    ok = pessoa_service.delete_pessoa(pessoa_id)
    if not ok:
        raise HTTPException(
            status_code=409,
            detail="Pessoa não pode ser removida pois está vinculada a um Funcionário"
        )
    return None