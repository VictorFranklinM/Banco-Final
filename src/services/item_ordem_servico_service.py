from daos import item_ordem_servico_dao

def list_all():
    return item_ordem_servico_dao.list_items()

def get(item_id: int):
    return item_ordem_servico_dao.get_item(item_id)

def create(data: dict):
    return item_ordem_servico_dao.create_item(data)

def update(item_id: int, data: dict):
    return item_ordem_servico_dao.update_item(item_id, data)

def delete(item_id: int):
    return item_ordem_servico_dao.delete_item(item_id)