from daos import status_ordem_servico_dao

def list_all():
    return status_ordem_servico_dao.list_status()

def get(status_id: int):
    return status_ordem_servico_dao.get_status(status_id)

def create(data: dict):
    return status_ordem_servico_dao.create_status(data)

def update(status_id: int, data: dict):
    return status_ordem_servico_dao.update_status(status_id, data)

def delete(status_id: int):
    return status_ordem_servico_dao.delete_status(status_id)