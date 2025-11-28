from daos import equipe_membro_dao

def list_all():
    return equipe_membro_dao.list_membros()

def get(membro_id: int):
    return equipe_membro_dao.get_membro(membro_id)

def create(data: dict):
    return equipe_membro_dao.create_membro(data)

def update(membro_id: int, data: dict):
    return equipe_membro_dao.update_membro(membro_id, data)

def delete(membro_id: int):
    return equipe_membro_dao.delete_membro(membro_id)