from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_funcionarios() -> List[dict]:
    sql = """SELECT id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao
             FROM funcionario ORDER BY id"""
    return fetchall(sql)

def get_funcionario(func_id: int) -> Optional[dict]:
    sql = "SELECT id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao FROM funcionario WHERE id = %s"
    return fetchone(sql, (func_id,))

def create_funcionario(data: dict) -> dict:
    sql = """INSERT INTO funcionario (pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao)
             VALUES (%s, %s, %s, %s, %s)
             RETURNING id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao"""
    return fetchone(sql, (data.get("pessoa_id"), data.get("tipo_funcionario_id"), data.get("setor_id"),
                          data.get("data_admissao"), data.get("data_demissao")))

def update_funcionario(func_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_funcionario(func_id)
    sql = f"UPDATE funcionario SET {', '.join(cols)} WHERE id = %s RETURNING id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao"
    vals.append(func_id)
    return fetchone(sql, tuple(vals))

def delete_funcionario(func_id: int) -> bool:
    sql = "DELETE FROM funcionario WHERE id = %s"
    try:
        execute(sql, (func_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False