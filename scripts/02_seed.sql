TRUNCATE TABLE movimento_estoque, estoque, item_ordem_servico, andamento_ordem_servico,
    ordem_servico, produto_variacao, produto, marca, unidade_medida, categoria_material,
    local_estoque, equipe_membro, equipe_manutencao, area_campus, tipo_area_campus,
    funcionario, pessoa, tipo_funcionario, setor, cor, tamanho, tipo_movimento_estoque,
    tipo_ordem_servico, status_ordem_servico RESTART IDENTITY CASCADE;

INSERT INTO pessoa (nome, cpf, matricula_siape, email, telefone, ativo) VALUES
  ('Ana Pereira', '11122233344', 'S001', 'ana.pereira@ifce.edu.br', '85-99991-0001', true),
  ('Bruno Oliveira', '22233344455', 'S002', 'bruno.oliveira@ifce.edu.br', '85-99991-0002', true),
  ('Carla Santos', '33344455566', 'S003', 'carla.santos@ifce.edu.br', '85-99991-0003', true);

INSERT INTO tipo_funcionario (id, descricao) VALUES
  (1, 'Jardineiro'),
  (2, 'Técnico'),
  (3, 'Supervisor');

INSERT INTO setor (id, nome, sigla) VALUES
  (1, 'Manutenção Predial', 'MP'),
  (2, 'Jardinagem', 'JAR'),
  (3, 'Almoxarifado', 'ALM');

INSERT INTO funcionario (id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao) VALUES
  (1, 1, 1, 2, '2020-03-01', NULL),
  (2, 2, 2, 1, '2019-08-15', NULL),
  (3, 3, 3, 1, '2018-01-10', NULL);

INSERT INTO tipo_area_campus (id, descricao) VALUES
  (1, 'Interna'),
  (2, 'Externa');

INSERT INTO area_campus (id, tipo_area_id, descricao, bloco) VALUES
  (1, 2, 'Bloco 3 - Jardins', '3'),
  (2, 2, 'Bloco 3 - Estacionamento', '3'),
  (3, 1, 'Biblioteca', '1');

INSERT INTO equipe_manutencao (id, nome, turno) VALUES
  (1, 'Equipe Verde', 'Manhã'),
  (2, 'Equipe Azul', 'Tarde');

INSERT INTO equipe_membro (id, equipe_id, funcionario_id, data_inicio, data_fim, funcao) VALUES
  (1, 1, 1, '2021-01-01', NULL, 'Operador'),
  (2, 1, 2, '2021-01-01', NULL, 'Apoio'),
  (3, 2, 3, '2022-05-01', NULL, 'Líder');

INSERT INTO categoria_material (id, nome) VALUES
  (1, 'Ferramentas manuais'),
  (2, 'Insumos');

INSERT INTO unidade_medida (id, sigla, descricao) VALUES
  (1, 'un', 'Unidade'),
  (2, 'kg', 'Quilograma');

INSERT INTO marca (id, nome) VALUES
  (1, 'MarcaForte'),
  (2, 'VerdeMais');

INSERT INTO produto (id, descricao, categoria_id, unidade_medida_id, marca_id) VALUES
  (1, 'Pá de jardim modelo X', 1, 1, 1),
  (2, 'Tesoura de poda profissional', 1, 1, 1),
  (3, 'Adubo orgânico 20kg', 2, 2, 2);

INSERT INTO cor (id, nome) VALUES
  (1, 'Preto'),
  (2, 'Verde');

INSERT INTO tamanho (id, descricao) VALUES
  (1, 'Padrão'),
  (2, 'Grande');

INSERT INTO produto_variacao (id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno) VALUES
  (1, 1, 1, 1, '7890000000001', 'P-JARD-001'),
  (2, 2, 1, 1, '7890000000002', 'T-PODA-001'),
  (3, 3, 2, 2, '7890000000003', 'ADUBO-20KG');

INSERT INTO local_estoque (id, descricao, responsavel_id) VALUES
  (1, 'Almoxarifado Central', 3),
  (2, 'Depósito Jardim', 2);

INSERT INTO estoque (produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao) VALUES
  (1, 1, 5.000, 2.000),
  (2, 1, 0.000, 1.000),
  (3, 1, 25.000, 10.000),
  (1, 2, 2.000, 2.000);

INSERT INTO tipo_movimento_estoque (id, descricao, sinal) VALUES
  (1, 'Entrada', '+'),
  (2, 'Saída', '-');

INSERT INTO movimento_estoque (id, produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao) VALUES
  (1, 1, 1, 2, 1.000, NOW(), 3, NULL, 'Uso em manutenção'),
  (2, 3, 1, 2, 5.000, NOW(), 3, NULL, 'Uso em poda'),
  (3, 3, 1, 1, 10.000, NOW(), 2, NULL, 'Reabastecimento');

INSERT INTO tipo_ordem_servico (id, descricao) VALUES
  (1, 'Manutenção'),
  (2, 'Limpeza');

INSERT INTO status_ordem_servico (id, descricao) VALUES
  (1, 'Aberta'),
  (2, 'Em Atendimento'),
  (3, 'Concluída'),
  (4, 'Cancelada');

INSERT INTO ordem_servico (id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema) VALUES
  (1, 'OS-2025-0001', 1, 1, 1, 1, 3, 1, 2, NOW(), (NOW() + INTERVAL '3 days')::DATE, 'Podar arbustos e recolher detritos'),
  (2, 'OS-2025-0002', 2, 2, 2, 2, 1, 1, 3, NOW(), (NOW() + INTERVAL '1 day')::DATE, 'Limpeza e varrição do estacionamento');

INSERT INTO item_ordem_servico (id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada) VALUES
  (1, 1, 1, 2.000, 1.000),
  (2, 1, 3, 5.000, 3.000),
  (3, 2, 2, 1.000, 0.000);

INSERT INTO andamento_ordem_servico (id, os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento) VALUES
  (1, 1, NOW(), 1, 2, 3, 'Equipe iniciou poda', NOW(), NULL),
  (2, 2, NOW(), 1, 2, 1, 'Limpeza iniciada', NOW(), NULL);
