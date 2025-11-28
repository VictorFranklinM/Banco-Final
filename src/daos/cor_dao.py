from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_cores() -> List[dict]:
    sql = "SELECT id, nome FROM cor ORDER BY id"
    return fetchall(sql)

def get_cor(cor_id: int) -> Optional[dict]:
    sql = "SELECT id, nome FROM cor WHERE id = %s"
    return fetchone(sql, (cor_id,))

def create_cor(data: dict) -> dict:
    sql = "INSERT INTO cor (nome) VALUES (%s) RETURNING id, nome"
    return fetchone(sql, (data.get("nome"),))

def update_cor(cor_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE cor SET nome = %s WHERE id = %s RETURNING id, nome"
    return fetchone(sql, (data.get("nome"), cor_id))

def delete_cor(cor_id: int) -> bool:
    sql = "DELETE FROM cor WHERE id = %s"
    try:
        execute(sql, (cor_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False