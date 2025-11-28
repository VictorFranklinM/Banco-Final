from database import fetchall

def ordens_abertas():
    sql = """
    SELECT os.id,
           os.numero_sequencial,
           os.prioridade,
           ac.descricao AS area,
           tos.descricao AS tipo_servico,
           p.nome AS solicitante,
           os.data_abertura
    FROM ordem_servico os
    JOIN area_campus ac ON os.area_campus_id = ac.id
    JOIN tipo_ordem_servico tos ON os.tipo_os_id = tos.id
    JOIN status_ordem_servico sts ON os.status_id = sts.id
    JOIN pessoa p ON os.solicitante_id = p.id
    WHERE LOWER(sts.descricao) IN ('aberta', 'em atendimento', 'aguardando material', 'aguardando')
    ORDER BY os.prioridade ASC, ac.descricao ASC, os.data_abertura ASC;
    """
    return fetchall(sql, ())

def materiais_abaixo_ponto():
    sql = """
    SELECT p.descricao       AS produto,
           pv.codigo_interno,
           le.descricao       AS local,
           e.quantidade,
           e.ponto_reposicao,
           (e.ponto_reposicao - e.quantidade) AS faltante
    FROM estoque e
    JOIN produto_variacao pv ON e.produto_variacao_id = pv.id
    JOIN produto p ON pv.produto_id = p.id
    JOIN local_estoque le ON e.local_estoque_id = le.id
    WHERE e.quantidade < e.ponto_reposicao
    ORDER BY (e.ponto_reposicao - e.quantidade) DESC;
    """
    return fetchall(sql, ())

def timeline_os(os_id: int):
    sql = """
    SELECT a.data_hora,
           pes.nome        AS funcionario,
           sts_novo.descricao AS status_atual,
           a.descricao
    FROM andamento_ordem_servico a
    LEFT JOIN funcionario f ON a.funcionario_id = f.id
    LEFT JOIN pessoa pes ON f.pessoa_id = pes.id
    LEFT JOIN status_ordem_servico sts_novo ON a.status_novo_id = sts_novo.id
    WHERE a.os_id = %s
    ORDER BY a.data_hora ASC;
    """
    return fetchall(sql, (os_id,))

def consumo_por_equipe(data_inicio: str, data_fim: str):
    sql = """
    SELECT eq.nome    AS equipe,
           p.descricao AS produto,
           SUM(
             CASE WHEN LOWER(tm.sinal) = '-' THEN -me.quantidade
                  ELSE me.quantidade END
           ) AS total_consumo
    FROM movimento_estoque me
    JOIN tipo_movimento_estoque tm ON me.tipo_movimento_id = tm.id
    JOIN produto_variacao pv ON me.produto_variacao_id = pv.id
    JOIN produto p ON pv.produto_id = p.id
    LEFT JOIN ordem_servico os ON me.ordem_servico_id = os.id
    LEFT JOIN equipe_manutencao eq ON os.equipe_id = eq.id
    WHERE me.data_hora BETWEEN %s AND %s
    GROUP BY eq.nome, p.descricao
    ORDER BY eq.nome, p.descricao;
    """
    return fetchall(sql, (data_inicio, data_fim))

def os_concluidas_por_tipo(ano: int):
    sql = """
    SELECT tos.descricao AS tipo_os,
           COUNT(*) AS total
    FROM ordem_servico os
    JOIN tipo_ordem_servico tos ON os.tipo_os_id = tos.id
    JOIN status_ordem_servico sts ON os.status_id = sts.id
    WHERE LOWER(sts.descricao) LIKE '%%conclu%%'
      AND EXTRACT(YEAR FROM os.data_abertura) = %s
    GROUP BY tos.descricao
    ORDER BY total DESC;
    """
    return fetchall(sql, (ano,))
