from daos import andamento_ordem_servico_dao

def list_all():
    return andamento_ordem_servico_dao.list_andamentos()

def get(andamento_id: int):
    return andamento_ordem_servico_dao.get_andamento(andamento_id)

def create(data: dict):
    return andamento_ordem_servico_dao.create_andamento(data)

def update(andamento_id: int, data: dict):
    return andamento_ordem_servico_dao.update_andamento(andamento_id, data)

def delete(andamento_id: int):
    return andamento_ordem_servico_dao.delete_andamento(andamento_id)
