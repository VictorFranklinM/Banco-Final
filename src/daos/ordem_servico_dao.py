from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_os() -> List[dict]:
    sql = """SELECT id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema
             FROM ordem_servico ORDER BY id"""
    return fetchall(sql)

def get_os(os_id: int) -> Optional[dict]:
    sql = "SELECT id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema FROM ordem_servico WHERE id = %s"
    return fetchone(sql, (os_id,))

def create_os(data: dict) -> dict:
    sql = """INSERT INTO ordem_servico (numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             RETURNING id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema"""
    return fetchone(sql, (data.get("numero_sequencial"), data.get("solicitante_id"), data.get("area_campus_id"),
                          data.get("tipo_os_id"), data.get("equipe_id"), data.get("lider_id"),
                          data.get("status_id"), data.get("prioridade"), data.get("data_abertura"), data.get("data_prevista"), data.get("descricao_problema")))

def update_os(os_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_os(os_id)
    sql = f"UPDATE ordem_servico SET {', '.join(cols)} WHERE id = %s RETURNING id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema"
    vals.append(os_id)
    return fetchone(sql, tuple(vals))

def delete_os(os_id: int) -> bool:
    sql = "DELETE FROM ordem_servico WHERE id = %s"
    try:
        execute(sql, (os_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False