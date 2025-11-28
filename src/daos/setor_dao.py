from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_setores() -> List[dict]:
    sql = "SELECT id, nome, sigla FROM setor ORDER BY id"
    return fetchall(sql)

def get_setor(setor_id: int) -> Optional[dict]:
    sql = "SELECT id, nome, sigla FROM setor WHERE id = %s"
    return fetchone(sql, (setor_id,))

def create_setor(data: dict) -> dict:
    sql = "INSERT INTO setor (nome, sigla) VALUES (%s, %s) RETURNING id, nome, sigla"
    return fetchone(sql, (data.get("nome"), data.get("sigla")))

def update_setor(setor_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_setor(setor_id)
    sql = f"UPDATE setor SET {', '.join(cols)} WHERE id = %s RETURNING id, nome, sigla"
    vals.append(setor_id)
    return fetchone(sql, tuple(vals))

def delete_setor(setor_id: int) -> bool:
    sql = "DELETE FROM setor WHERE id = %s"
    try:
        execute(sql, (setor_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False
