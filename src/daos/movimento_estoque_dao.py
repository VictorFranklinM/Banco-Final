from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_movimentos() -> List[dict]:
    sql = """SELECT id, produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao
             FROM movimento_estoque ORDER BY id"""
    return fetchall(sql)

def get_movimento(mov_id: int) -> Optional[dict]:
    sql = "SELECT id, produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao FROM movimento_estoque WHERE id = %s"
    return fetchone(sql, (mov_id,))

def create_movimento(data: dict) -> dict:
    sql = """INSERT INTO movimento_estoque (produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
             RETURNING id, produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao"""
    return fetchone(sql, (data.get("produto_variacao_id"), data.get("local_estoque_id"), data.get("tipo_movimento_id"), data.get("quantidade"), data.get("data_hora"), data.get("funcionario_id"), data.get("ordem_servico_id"), data.get("observacao")))

def update_movimento(mov_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_movimento(mov_id)
    sql = f"UPDATE movimento_estoque SET {', '.join(cols)} WHERE id = %s RETURNING id, produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao"
    vals.append(mov_id)
    return fetchone(sql, tuple(vals))

def delete_movimento(mov_id: int) -> bool:
    sql = "DELETE FROM movimento_estoque WHERE id = %s"
    try:
        execute(sql, (mov_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False
