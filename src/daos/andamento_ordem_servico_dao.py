from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_andamentos() -> List[dict]:
    sql = """SELECT id, os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento
             FROM andamento_ordem_servico ORDER BY id"""
    return fetchall(sql)

def get_andamento(andamento_id: int) -> Optional[dict]:
    sql = "SELECT id, os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento FROM andamento_ordem_servico WHERE id = %s"
    return fetchone(sql, (andamento_id,))

def create_andamento(data: dict) -> dict:
    sql = """INSERT INTO andamento_ordem_servico (os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
             RETURNING id, os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento"""
    return fetchone(sql, (data.get("os_id"), data.get("data_hora"), data.get("status_anterior_id"), data.get("status_novo_id"), data.get("funcionario_id"), data.get("descricao"), data.get("inicio_atendimento"), data.get("fim_atendimento")))

def update_andamento(andamento_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_andamento(andamento_id)
    sql = f"UPDATE andamento_ordem_servico SET {', '.join(cols)} WHERE id = %s RETURNING id, os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento"
    vals.append(andamento_id)
    return fetchone(sql, tuple(vals))

def delete_andamento(andamento_id: int) -> bool:
    sql = "DELETE FROM andamento_ordem_servico WHERE id = %s"
    try:
        execute(sql, (andamento_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False