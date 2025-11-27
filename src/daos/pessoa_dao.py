from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_pessoas(limit: int = 100, offset: int = 0) -> List[dict]:
    sql = "SELECT id, nome, cpf, matricula_siape, email, telefone, ativo FROM pessoa ORDER BY id LIMIT %s OFFSET %s"
    return fetchall(sql, (limit, offset))

def get_pessoa(pessoa_id: int) -> Optional[dict]:
    sql = "SELECT id, nome, cpf, matricula_siape, email, telefone, ativo FROM pessoa WHERE id = %s"
    return fetchone(sql, (pessoa_id,))

def create_pessoa(data: dict) -> dict:
    sql = """
    INSERT INTO pessoa (nome, cpf, matricula_siape, email, telefone, ativo)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING id, nome, cpf, matricula_siape, email, telefone, ativo
    """
    return fetchone(sql, (data.get("nome"), data.get("cpf"), data.get("matricula_siape"),
                          data.get("email"), data.get("telefone"), data.get("ativo")))

def update_pessoa(pessoa_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_pessoa(pessoa_id)
    sql = f"UPDATE pessoa SET {', '.join(cols)} WHERE id = %s RETURNING id, nome, cpf, matricula_siape, email, telefone, ativo"
    vals.append(pessoa_id)
    return fetchone(sql, tuple(vals))

def delete_pessoa(pessoa_id: int):
    sql = "DELETE FROM pessoa WHERE id = %s"
    try:
        execute(sql, (pessoa_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False