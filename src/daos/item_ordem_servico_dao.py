from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_items() -> List[dict]:
    sql = "SELECT id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada FROM item_ordem_servico ORDER BY id"
    return fetchall(sql)

def get_item(item_id: int) -> Optional[dict]:
    sql = "SELECT id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada FROM item_ordem_servico WHERE id = %s"
    return fetchone(sql, (item_id,))

def create_item(data: dict) -> dict:
    sql = "INSERT INTO item_ordem_servico (os_id, produto_variacao_id, quantidade_prevista, quantidade_usada) VALUES (%s, %s, %s, %s) RETURNING id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada"
    return fetchone(sql, (data.get("os_id"), data.get("produto_variacao_id"), data.get("quantidade_prevista"), data.get("quantidade_usada")))

def update_item(item_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_item(item_id)
    sql = f"UPDATE item_ordem_servico SET {', '.join(cols)} WHERE id = %s RETURNING id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada"
    vals.append(item_id)
    return fetchone(sql, tuple(vals))

def delete_item(item_id: int) -> bool:
    sql = "DELETE FROM item_ordem_servico WHERE id = %s"
    try:
        execute(sql, (item_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False