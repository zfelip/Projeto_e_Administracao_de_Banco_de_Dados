from services.activity import ActivityService

class ActivityController:
    def __init__(self, service):
        self.service = service

    def criar(self, data):
        return self.service.criar_atividade(data)

    def listar(self):
        return self.service.listar()

    def atualizar(self, activity_id, data):
        return self.service.atualizar(activity_id, data)

    def remover(self, activity_id):
        return self.service.remover(activity_id)

    def andamento_com_responsavel(self):
        return self.service.atividades_em_andamento()

    def resumo_status(self):
        return self.service.resumo_por_status()
