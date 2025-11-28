from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_tipos() -> List[dict]:
    sql = "SELECT id, descricao, sinal FROM tipo_movimento_estoque ORDER BY id"
    return fetchall(sql)

def get_tipo(tipo_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao, sinal FROM tipo_movimento_estoque WHERE id = %s"
    return fetchone(sql, (tipo_id,))

def create_tipo(data: dict) -> dict:
    sql = "INSERT INTO tipo_movimento_estoque (descricao, sinal) VALUES (%s, %s) RETURNING id, descricao, sinal"
    return fetchone(sql, (data.get("descricao"), data.get("sinal")))

def update_tipo(tipo_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_tipo(tipo_id)
    sql = f"UPDATE tipo_movimento_estoque SET {', '.join(cols)} WHERE id = %s RETURNING id, descricao, sinal"
    vals.append(tipo_id)
    return fetchone(sql, tuple(vals))

def delete_tipo(tipo_id: int) -> bool:
    sql = "DELETE FROM tipo_movimento_estoque WHERE id = %s"
    try:
        execute(sql, (tipo_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False