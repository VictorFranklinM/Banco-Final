from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_locais() -> List[dict]:
    sql = "SELECT id, descricao, responsavel_id FROM local_estoque ORDER BY id"
    return fetchall(sql)

def get_local(local_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao, responsavel_id FROM local_estoque WHERE id = %s"
    return fetchone(sql, (local_id,))

def create_local(data: dict) -> dict:
    sql = "INSERT INTO local_estoque (descricao, responsavel_id) VALUES (%s, %s) RETURNING id, descricao, responsavel_id"
    return fetchone(sql, (data.get("descricao"), data.get("responsavel_id")))

def update_local(local_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_local(local_id)
    sql = f"UPDATE local_estoque SET {', '.join(cols)} WHERE id = %s RETURNING id, descricao, responsavel_id"
    vals.append(local_id)
    return fetchone(sql, tuple(vals))

def delete_local(local_id: int) -> bool:
    sql = "DELETE FROM local_estoque WHERE id = %s"
    try:
        execute(sql, (local_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False