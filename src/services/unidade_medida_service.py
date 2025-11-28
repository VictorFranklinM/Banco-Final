from daos import unidade_medida_dao

def list_all():
    return unidade_medida_dao.list_unidades()

def get(unidade_id: int):
    return unidade_medida_dao.get_unidade(unidade_id)

def create(data: dict):
    return unidade_medida_dao.create_unidade(data)

def update(unidade_id: int, data: dict):
    return unidade_medida_dao.update_unidade(unidade_id, data)

def delete(unidade_id: int):
    return unidade_medida_dao.delete_unidade(unidade_id)