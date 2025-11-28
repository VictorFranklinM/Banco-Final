from daos import cor_dao

def list_all():
    return cor_dao.list_cores()

def get(cor_id: int):
    return cor_dao.get_cor(cor_id)

def create(data: dict):
    return cor_dao.create_cor(data)

def update(cor_id: int, data: dict):
    return cor_dao.update_cor(cor_id, data)

def delete(cor_id: int):
    return cor_dao.delete_cor(cor_id)