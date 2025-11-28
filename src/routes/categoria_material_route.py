from fastapi import APIRouter, HTTPException
from typing import List
from models.categoria_material import CategoriaMaterialIn, CategoriaMaterialOut
from services import categoria_material_service

router = APIRouter()

@router.get("/", response_model=List[CategoriaMaterialOut])
def listar():
    return categoria_material_service.list_all()

@router.get("/{cat_id}", response_model=CategoriaMaterialOut)
def obter(cat_id: int):
    c = categoria_material_service.get(cat_id)
    if not c:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return c

@router.post("/", response_model=CategoriaMaterialOut, status_code=201)
def criar(payload: CategoriaMaterialIn):
    return categoria_material_service.create(payload.dict())

@router.put("/{cat_id}", response_model=CategoriaMaterialOut)
def atualizar(cat_id: int, payload: CategoriaMaterialIn):
    updated = categoria_material_service.update(cat_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return updated

@router.delete("/{cat_id}", status_code=204)
def remover(cat_id: int):
    ok = categoria_material_service.delete(cat_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None