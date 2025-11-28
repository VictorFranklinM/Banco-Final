from daos import consultas_dao

class ConsultasService:

    def listar_ordens_abertas(self):
        return consultas_dao.ordens_abertas()

    def listar_materiais_criticos(self):
        return consultas_dao.materiais_abaixo_ponto()

    def listar_timeline_os(self, os_id: int):
        return consultas_dao.timeline_os(os_id)

    def listar_consumo_por_equipe(self, data_inicio: str, data_fim: str):
        return consultas_dao.consumo_por_equipe(data_inicio, data_fim)

    def listar_os_concluidas_por_tipo(self, ano: int):
        return consultas_dao.os_concluidas_por_tipo(ano)

consultas_service = ConsultasService()