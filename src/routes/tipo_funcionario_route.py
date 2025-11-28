from fastapi import APIRouter, HTTPException
from typing import List
from models.tipo_funcionario import TipoFuncionarioIn, TipoFuncionarioOut
from services import tipo_funcionario_service

router = APIRouter()

@router.get("/", response_model=List[TipoFuncionarioOut])
def listar_tipos_funcionarios():
    return tipo_funcionario_service.list_tipos_funcionarios()

@router.get("/{tipo_id}", response_model=TipoFuncionarioOut)
def obter_tipo_funcionario(tipo_id: int):
    t = tipo_funcionario_service.get_tipo_funcionario(tipo_id)
    if not t:
        raise HTTPException(status_code=404, detail="Tipo de funcionário não encontrado")
    return t

@router.post("/", response_model=TipoFuncionarioOut, status_code=201)
def criar_tipo_funcionario(payload: TipoFuncionarioIn):
    return tipo_funcionario_service.create_tipo_funcionario(payload.dict())

@router.put("/{tipo_id}", response_model=TipoFuncionarioOut)
def atualizar_tipo_funcionario(tipo_id: int, payload: TipoFuncionarioIn):
    updated = tipo_funcionario_service.update_tipo_funcionario(tipo_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Tipo de funcionário não encontrado")
    return updated

@router.delete("/{tipo_id}", status_code=204)
def remover_tipo_funcionario(tipo_id: int):
    ok = tipo_funcionario_service.delete_tipo_funcionario(tipo_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None