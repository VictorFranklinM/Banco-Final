from daos import equipe_manutencao_dao

def list_all():
    return equipe_manutencao_dao.list_equipes()

def get(equipe_id: int):
    return equipe_manutencao_dao.get_equipe(equipe_id)

def create(data: dict):
    return equipe_manutencao_dao.create_equipe(data)

def update(equipe_id: int, data: dict):
    return equipe_manutencao_dao.update_equipe(equipe_id, data)

def delete(equipe_id: int):
    return equipe_manutencao_dao.delete_equipe(equipe_id)