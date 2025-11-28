from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_variacoes() -> List[dict]:
    sql = "SELECT id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno FROM produto_variacao ORDER BY id"
    return fetchall(sql)

def get_variacao(var_id: int) -> Optional[dict]:
    sql = "SELECT id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno FROM produto_variacao WHERE id = %s"
    return fetchone(sql, (var_id,))

def create_variacao(data: dict) -> dict:
    sql = "INSERT INTO produto_variacao (produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno) VALUES (%s, %s, %s, %s, %s) RETURNING id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno"
    return fetchone(sql, (data.get("produto_id"), data.get("cor_id"), data.get("tamanho_id"), data.get("codigo_barras"), data.get("codigo_interno")))

def update_variacao(var_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_variacao(var_id)
    sql = f"UPDATE produto_variacao SET {', '.join(cols)} WHERE id = %s RETURNING id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno"
    vals.append(var_id)
    return fetchone(sql, tuple(vals))

def delete_variacao(var_id: int) -> bool:
    sql = "DELETE FROM produto_variacao WHERE id = %s"
    try:
        execute(sql, (var_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False