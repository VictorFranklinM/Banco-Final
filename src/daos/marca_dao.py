from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_marcas() -> List[dict]:
    sql = "SELECT id, nome FROM marca ORDER BY id"
    return fetchall(sql)

def get_marca(marca_id: int) -> Optional[dict]:
    sql = "SELECT id, nome FROM marca WHERE id = %s"
    return fetchone(sql, (marca_id,))

def create_marca(data: dict) -> dict:
    sql = "INSERT INTO marca (nome) VALUES (%s) RETURNING id, nome"
    return fetchone(sql, (data.get("nome"),))

def update_marca(marca_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE marca SET nome = %s WHERE id = %s RETURNING id, nome"
    return fetchone(sql, (data.get("nome"), marca_id))

def delete_marca(marca_id: int) -> bool:
    sql = "DELETE FROM marca WHERE id = %s"
    try:
        execute(sql, (marca_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False