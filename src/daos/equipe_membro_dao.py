from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_membros() -> List[dict]:
    sql = "SELECT id, equipe_id, funcionario_id, data_inicio, data_fim, funcao FROM equipe_membro ORDER BY id"
    return fetchall(sql)

def get_membro(membro_id: int) -> Optional[dict]:
    sql = "SELECT id, equipe_id, funcionario_id, data_inicio, data_fim, funcao FROM equipe_membro WHERE id = %s"
    return fetchone(sql, (membro_id,))

def create_membro(data: dict) -> dict:
    sql = "INSERT INTO equipe_membro (equipe_id, funcionario_id, data_inicio, data_fim, funcao) VALUES (%s, %s, %s, %s, %s) RETURNING id, equipe_id, funcionario_id, data_inicio, data_fim, funcao"
    return fetchone(sql, (data.get("equipe_id"), data.get("funcionario_id"), data.get("data_inicio"), data.get("data_fim"), data.get("funcao")))

def update_membro(membro_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_membro(membro_id)
    sql = f"UPDATE equipe_membro SET {', '.join(cols)} WHERE id = %s RETURNING id, equipe_id, funcionario_id, data_inicio, data_fim, funcao"
    vals.append(membro_id)
    return fetchone(sql, tuple(vals))

def delete_membro(membro_id: int) -> bool:
    sql = "DELETE FROM equipe_membro WHERE id = %s"
    try:
        execute(sql, (membro_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return Falsecategoria_material_dao