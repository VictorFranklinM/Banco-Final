from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_categorias() -> List[dict]:
    sql = "SELECT id, nome FROM categoria_material ORDER BY id"
    return fetchall(sql)

def get_categoria(cat_id: int) -> Optional[dict]:
    sql = "SELECT id, nome FROM categoria_material WHERE id = %s"
    return fetchone(sql, (cat_id,))

def create_categoria(data: dict) -> dict:
    sql = "INSERT INTO categoria_material (nome) VALUES (%s) RETURNING id, nome"
    return fetchone(sql, (data.get("nome"),))

def update_categoria(cat_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE categoria_material SET nome = %s WHERE id = %s RETURNING id, nome"
    return fetchone(sql, (data.get("nome"), cat_id))

def delete_categoria(cat_id: int) -> bool:
    sql = "DELETE FROM categoria_material WHERE id = %s"
    try:
        execute(sql, (cat_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False