from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_produtos() -> List[dict]:
    sql = "SELECT id, descricao, categoria_id, unidade_medida_id, marca_id FROM produto ORDER BY id"
    return fetchall(sql)

def get_produto(produto_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao, categoria_id, unidade_medida_id, marca_id FROM produto WHERE id = %s"
    return fetchone(sql, (produto_id,))

def create_produto(data: dict) -> dict:
    sql = "INSERT INTO produto (descricao, categoria_id, unidade_medida_id, marca_id) VALUES (%s, %s, %s, %s) RETURNING id, descricao, categoria_id, unidade_medida_id, marca_id"
    return fetchone(sql, (data.get("descricao"), data.get("categoria_id"), data.get("unidade_medida_id"), data.get("marca_id")))

def update_produto(produto_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_produto(produto_id)
    sql = f"UPDATE produto SET {', '.join(cols)} WHERE id = %s RETURNING id, descricao, categoria_id, unidade_medida_id, marca_id"
    vals.append(produto_id)
    return fetchone(sql, tuple(vals))

def delete_produto(produto_id: int) -> bool:
    sql = "DELETE FROM produto WHERE id = %s"
    try:
        execute(sql, (produto_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False