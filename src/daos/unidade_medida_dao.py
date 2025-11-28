from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_unidades() -> List[dict]:
    sql = "SELECT id, sigla, descricao FROM unidade_medida ORDER BY id"
    return fetchall(sql)

def get_unidade(unidade_id: int) -> Optional[dict]:
    sql = "SELECT id, sigla, descricao FROM unidade_medida WHERE id = %s"
    return fetchone(sql, (unidade_id,))

def create_unidade(data: dict) -> dict:
    sql = "INSERT INTO unidade_medida (sigla, descricao) VALUES (%s, %s) RETURNING id, sigla, descricao"
    return fetchone(sql, (data.get("sigla"), data.get("descricao")))

def update_unidade(unidade_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_unidade(unidade_id)
    sql = f"UPDATE unidade_medida SET {', '.join(cols)} WHERE id = %s RETURNING id, sigla, descricao"
    vals.append(unidade_id)
    return fetchone(sql, tuple(vals))

def delete_unidade(unidade_id: int) -> bool:
    sql = "DELETE FROM unidade_medida WHERE id = %s"
    try:
        execute(sql, (unidade_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False