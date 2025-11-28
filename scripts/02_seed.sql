TRUNCATE TABLE movimento_estoque, estoque, item_ordem_servico, andamento_ordem_servico,
    ordem_servico, produto_variacao, produto, marca, unidade_medida, categoria_material,
    local_estoque, equipe_membro, equipe_manutencao, area_campus, tipo_area_campus,
    funcionario, pessoa, tipo_funcionario, setor, cor, tamanho, tipo_movimento_estoque,
    tipo_ordem_servico, status_ordem_servico RESTART IDENTITY CASCADE;

INSERT INTO pessoa (nome, cpf, matricula_siape, email, telefone, ativo) VALUES
  ('Ana Pereira', '11122233344', 'S001', 'ana.pereira@ifce.edu.br', '85-99991-0001', true),
  ('Bruno Oliveira', '22233344455', 'S002', 'bruno.oliveira@ifce.edu.br', '85-99991-0002', true),
  ('Carla Santos', '33344455566', 'S003', 'carla.santos@ifce.edu.br', '85-99991-0003', true),
  ('Diego Ramos', '44455566677', 'S004', 'diego.ramos@ifce.edu.br', '85-99991-0004', true),
  ('Elaine Costa', '55566677788', 'S005', 'elaine.costa@ifce.edu.br', '85-99991-0005', true);

INSERT INTO tipo_funcionario (descricao) VALUES
  ('Jardineiro'),
  ('Técnico'),
  ('Supervisor');

INSERT INTO setor (nome, sigla) VALUES
  ('Manutenção Predial', 'MP'),
  ('Jardinagem', 'JAR'),
  ('Almoxarifado', 'ALM');

INSERT INTO funcionario (pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao) VALUES
  ((SELECT id FROM pessoa WHERE nome='Ana Pereira'), 1, 2, '2020-03-01', NULL),
  ((SELECT id FROM pessoa WHERE nome='Bruno Oliveira'), 2, 1, '2019-08-15', NULL),
  ((SELECT id FROM pessoa WHERE nome='Carla Santos'), 3, 1, '2018-01-10', NULL),
  ((SELECT id FROM pessoa WHERE nome='Diego Ramos'), 1, 2, '2021-07-01', NULL),
  ((SELECT id FROM pessoa WHERE nome='Elaine Costa'), 2, 3, '2022-02-10', NULL);

INSERT INTO tipo_area_campus (descricao) VALUES
  ('Interna'),
  ('Externa');

INSERT INTO area_campus (tipo_area_id, descricao, bloco) VALUES
  ((SELECT id FROM tipo_area_campus WHERE descricao='Externa'), 'Bloco 3 - Jardins', '3'),
  ((SELECT id FROM tipo_area_campus WHERE descricao='Externa'), 'Bloco 3 - Estacionamento', '3'),
  ((SELECT id FROM tipo_area_campus WHERE descricao='Interna'), 'Biblioteca', '1'),
  ((SELECT id FROM tipo_area_campus WHERE descricao='Externa'), 'Praça Central', '0');

INSERT INTO equipe_manutencao (nome, turno) VALUES
  ('Equipe Manhã', 'Manhã'),
  ('Equipe Tarde', 'Tarde'),
  ('Equipe Extra', 'Noite');

INSERT INTO equipe_membro (equipe_id, funcionario_id, data_inicio, data_fim, funcao) VALUES
  ((SELECT id FROM equipe_manutencao WHERE nome='Equipe Manhã'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Ana Pereira')), '2021-01-01', NULL, 'Operador'),
  ((SELECT id FROM equipe_manutencao WHERE nome='Equipe Manhã'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira')), '2021-01-01', NULL, 'Apoio'),
  ((SELECT id FROM equipe_manutencao WHERE nome='Equipe Tarde'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Carla Santos')), '2022-05-01', NULL, 'Líder'),
  ((SELECT id FROM equipe_manutencao WHERE nome='Equipe Extra'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Diego Ramos')), '2023-03-01', NULL, 'Operador');

INSERT INTO categoria_material (nome) VALUES
  ('Ferramentas manuais'),
  ('Insumos'),
  ('PEÇAS');

INSERT INTO unidade_medida (sigla, descricao) VALUES
  ('un', 'Unidade'),
  ('kg', 'Quilograma'),
  ('m', 'Metro');

INSERT INTO marca (nome) VALUES
  ('MarcaForte'),
  ('VerdeMais'),
  ('EcoTools');

INSERT INTO produto (descricao, categoria_id, unidade_medida_id, marca_id) VALUES
  ('Pá de jardim modelo X', 1, 1, 1),
  ('Tesoura de poda profissional', 1, 1, 1),
  ('Adubo orgânico 20kg', 2, 2, 2),
  ('Mangueira 10m', 3, 3, 3);

INSERT INTO cor (nome) VALUES ('Preto'), ('Verde'), ('Amarelo');
INSERT INTO tamanho (descricao) VALUES ('Padrão'), ('Grande'), ('Pequeno');

INSERT INTO produto_variacao (produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno) VALUES
  ((SELECT id FROM produto WHERE descricao='Pá de jardim modelo X'), (SELECT id FROM cor WHERE nome='Preto'), (SELECT id FROM tamanho WHERE descricao='Padrão'), '7890000000001', 'P-JARD-001'),
  ((SELECT id FROM produto WHERE descricao='Tesoura de poda profissional'), (SELECT id FROM cor WHERE nome='Preto'), (SELECT id FROM tamanho WHERE descricao='Padrão'), '7890000000002', 'T-PODA-001'),
  ((SELECT id FROM produto WHERE descricao='Adubo orgânico 20kg'), (SELECT id FROM cor WHERE nome='Verde'), (SELECT id FROM tamanho WHERE descricao='Grande'), '7890000000003', 'ADUBO-20KG'),
  ((SELECT id FROM produto WHERE descricao='Mangueira 10m'), (SELECT id FROM cor WHERE nome='Amarelo'), (SELECT id FROM tamanho WHERE descricao='Padrão'), '7890000000004', 'MANG-10M');

INSERT INTO local_estoque (descricao, responsavel_id) VALUES
  ('Almoxarifado Central', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa'))),
  ('Depósito Jardim', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira'))),
  ('Depósito Externo', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Diego Ramos')));

INSERT INTO estoque (produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao) VALUES
  ((SELECT id FROM produto_variacao WHERE codigo_interno='P-JARD-001'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), 5.000, 2.000),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='T-PODA-001'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), 0.000, 1.000),  -- abaixo
  ((SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), 25.000, 10.000),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='P-JARD-001'), (SELECT id FROM local_estoque WHERE descricao='Depósito Jardim'), 1.000, 2.000), -- abaixo
  ((SELECT id FROM produto_variacao WHERE codigo_interno='MANG-10M'), (SELECT id FROM local_estoque WHERE descricao='Depósito Externo'), 0.500, 1.000); -- abaixo

INSERT INTO tipo_movimento_estoque (descricao, sinal) VALUES
  ('Entrada', '+'),
  ('Saída', '-');

INSERT INTO tipo_ordem_servico (descricao) VALUES
  ('Manutenção'),
  ('Limpeza'),
  ('Reforma');

INSERT INTO status_ordem_servico (descricao) VALUES
  ('Aberta'),
  ('Em Atendimento'),
  ('Aguardando Material'),
  ('Concluída'),
  ('Cancelada');

INSERT INTO ordem_servico
  (numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema)
VALUES
  ('OS-2025-0001', (SELECT id FROM pessoa WHERE nome='Ana Pereira'), (SELECT id FROM area_campus WHERE descricao='Bloco 3 - Jardins'),
     (SELECT id FROM tipo_ordem_servico WHERE descricao='Manutenção'),
     (SELECT id FROM equipe_manutencao WHERE nome='Equipe Manhã'),
     (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Carla Santos')),
     (SELECT id FROM status_ordem_servico WHERE descricao='Aberta'),
     2, '2025-11-01 09:00:00', '2025-11-04'::DATE, 'Podar arbustos e recolher detritos'),
  ('OS-2025-0002', (SELECT id FROM pessoa WHERE nome='Bruno Oliveira'), (SELECT id FROM area_campus WHERE descricao='Bloco 3 - Estacionamento'),
     (SELECT id FROM tipo_ordem_servico WHERE descricao='Limpeza'),
     (SELECT id FROM equipe_manutencao WHERE nome='Equipe Tarde'),
     (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Ana Pereira')),
     (SELECT id FROM status_ordem_servico WHERE descricao='Em Atendimento'),
     3, '2025-11-02 08:00:00', '2025-11-03'::DATE, 'Limpeza e varrição do estacionamento'),
  ('OS-2025-0003', (SELECT id FROM pessoa WHERE nome='Carla Santos'), (SELECT id FROM area_campus WHERE descricao='Praça Central'),
     (SELECT id FROM tipo_ordem_servico WHERE descricao='Manutenção'),
     (SELECT id FROM equipe_manutencao WHERE nome='Equipe Extra'),
     (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Diego Ramos')),
     (SELECT id FROM status_ordem_servico WHERE descricao='Aguardando Material'),
     1, '2025-10-10 10:00:00', '2025-10-12'::DATE, 'Reparo em regador central'),
  ('OS-2025-0004', (SELECT id FROM pessoa WHERE nome='Elaine Costa'), (SELECT id FROM area_campus WHERE descricao='Biblioteca'),
     (SELECT id FROM tipo_ordem_servico WHERE descricao='Reforma'),
     (SELECT id FROM equipe_manutencao WHERE nome='Equipe Manhã'),
     (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')),
     (SELECT id FROM status_ordem_servico WHERE descricao='Concluída'),
     2, '2025-06-15 14:00:00', '2025-06-20'::DATE, 'Pintura e reparos'),
  ('OS-2024-0001', (SELECT id FROM pessoa WHERE nome='Ana Pereira'), (SELECT id FROM area_campus WHERE descricao='Bloco 3 - Jardins'),
     (SELECT id FROM tipo_ordem_servico WHERE descricao='Limpeza'),
     (SELECT id FROM equipe_manutencao WHERE nome='Equipe Tarde'),
     (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira')),
     (SELECT id FROM status_ordem_servico WHERE descricao='Concluída'),
     4, '2024-09-01 07:30:00', '2024-09-02'::DATE, 'Limpeza geral pós-evento');

INSERT INTO item_ordem_servico (os_id, produto_variacao_id, quantidade_prevista, quantidade_usada) VALUES
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), (SELECT id FROM produto_variacao WHERE codigo_interno='P-JARD-001'), 2.000, 1.000),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), (SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), 5.000, 3.000),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0002'), (SELECT id FROM produto_variacao WHERE codigo_interno='T-PODA-001'), 1.000, 0.000),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0004'), (SELECT id FROM produto_variacao WHERE codigo_interno='MANG-10M'), 1.000, 1.000);

INSERT INTO andamento_ordem_servico
  (os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao, inicio_atendimento, fim_atendimento)
VALUES
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), '2025-11-01 09:05:00', (SELECT id FROM status_ordem_servico WHERE descricao='Aberta'), (SELECT id FROM status_ordem_servico WHERE descricao='Em Atendimento'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Carla Santos')), 'Equipe iniciou poda', '2025-11-01 09:05:00', NULL),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0004'), '2025-06-15 14:10:00', (SELECT id FROM status_ordem_servico WHERE descricao='Aberta'), (SELECT id FROM status_ordem_servico WHERE descricao='Em Atendimento'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')), 'Início dos reparos', '2025-06-15 14:10:00', '2025-06-17 12:00:00'),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0004'), '2025-06-19 16:00:00', (SELECT id FROM status_ordem_servico WHERE descricao='Em Atendimento'), (SELECT id FROM status_ordem_servico WHERE descricao='Concluída'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')), 'Serviços finalizados', '2025-06-19 09:00:00', '2025-06-19 16:00:00'),
  ((SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0003'), '2025-10-10 10:15:00', (SELECT id FROM status_ordem_servico WHERE descricao='Aberta'), (SELECT id FROM status_ordem_servico WHERE descricao='Aguardando Material'), (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Diego Ramos')), 'Aguardando chegada de peças', '2025-10-10 10:15:00', NULL);

INSERT INTO movimento_estoque
  (produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao)
VALUES
  ((SELECT id FROM produto_variacao WHERE codigo_interno='P-JARD-001'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 1.000, '2025-10-05 08:30:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')), (SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), 'Uso em poda'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 3.000, '2025-10-06 09:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')), (SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), 'Uso em podas'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='T-PODA-001'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 1.000, '2025-10-12 07:30:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Carla Santos')), (SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0002'), 'Uso em limpeza'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Entrada'), 10.000, '2025-10-20 10:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira')), NULL, 'Reabastecimento'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='MANG-10M'), (SELECT id FROM local_estoque WHERE descricao='Depósito Externo'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 0.200, '2025-10-22 15:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Diego Ramos')), NULL, 'Uso em rega'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='P-JARD-001'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 2.000, '2024-08-10 09:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira')), NULL, 'Uso antigo');

INSERT INTO movimento_estoque (produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade, data_hora, funcionario_id, ordem_servico_id, observacao)
VALUES
  ((SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Saída'), 2.000, '2025-10-25 08:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Elaine Costa')), (SELECT id FROM ordem_servico WHERE numero_sequencial='OS-2025-0001'), 'Uso em complemento'),
  ((SELECT id FROM produto_variacao WHERE codigo_interno='ADUBO-20KG'), (SELECT id FROM local_estoque WHERE descricao='Almoxarifado Central'), (SELECT id FROM tipo_movimento_estoque WHERE descricao='Entrada'), 5.000, '2025-09-01 10:00:00', (SELECT id FROM funcionario WHERE pessoa_id=(SELECT id FROM pessoa WHERE nome='Bruno Oliveira')), NULL, 'Compra estoque');
