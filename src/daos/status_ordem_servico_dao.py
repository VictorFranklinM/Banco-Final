from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_status() -> List[dict]:
    sql = "SELECT id, descricao FROM status_ordem_servico ORDER BY id"
    return fetchall(sql)

def get_status(status_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao FROM status_ordem_servico WHERE id = %s"
    return fetchone(sql, (status_id,))

def create_status(data: dict) -> dict:
    sql = "INSERT INTO status_ordem_servico (descricao) VALUES (%s) RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"),))

def update_status(status_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE status_ordem_servico SET descricao = %s WHERE id = %s RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"), status_id))

def delete_status(status_id: int) -> bool:
    sql = "DELETE FROM status_ordem_servico WHERE id = %s"
    try:
        execute(sql, (status_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False