from daos import ordem_servico_dao

def list_all():
    return ordem_servico_dao.list_os()

def get(os_id: int):
    return ordem_servico_dao.get_os(os_id)

def create(data: dict):
    return ordem_servico_dao.create_os(data)

def update(os_id: int, data: dict):
    return ordem_servico_dao.update_os(os_id, data)

def delete(os_id: int):
    return ordem_servico_dao.delete_os(os_id)