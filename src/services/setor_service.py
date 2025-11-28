from daos import setor_dao

def list_all():
    return setor_dao.list_setores()

def get(setor_id: int):
    return setor_dao.get_setor(setor_id)

def create(data: dict):
    return setor_dao.create_setor(data)

def update(setor_id: int, data: dict):
    return setor_dao.update_setor(setor_id, data)

def delete(setor_id: int):
    return setor_dao.delete_setor(setor_id)