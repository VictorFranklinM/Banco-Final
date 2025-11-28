from typing import List, Optional, Tuple
from database import fetchall, fetchone, execute
import psycopg2

def list_estoque() -> List[dict]:
    sql = "SELECT produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao FROM estoque ORDER BY produto_variacao_id"
    return fetchall(sql)

def get_estoque(produto_variacao_id: int, local_estoque_id: int) -> Optional[dict]:
    sql = "SELECT produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao FROM estoque WHERE produto_variacao_id = %s AND local_estoque_id = %s"
    return fetchone(sql, (produto_variacao_id, local_estoque_id))

def create_estoque(data: dict) -> dict:
    sql = "INSERT INTO estoque (produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao) VALUES (%s, %s, %s, %s) RETURNING produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao"
    return fetchone(sql, (data.get("produto_variacao_id"), data.get("local_estoque_id"), data.get("quantidade", 0), data.get("ponto_reposicao", 0)))

def update_estoque(produto_variacao_id: int, local_estoque_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_estoque(produto_variacao_id, local_estoque_id)
    sql = f"UPDATE estoque SET {', '.join(cols)} WHERE produto_variacao_id = %s AND local_estoque_id = %s RETURNING produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao"
    vals.extend([produto_variacao_id, local_estoque_id])
    return fetchone(sql, tuple(vals))

def delete_estoque(produto_variacao_id: int, local_estoque_id: int) -> bool:
    sql = "DELETE FROM estoque WHERE produto_variacao_id = %s AND local_estoque_id = %s"
    try:
        execute(sql, (produto_variacao_id, local_estoque_id))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False