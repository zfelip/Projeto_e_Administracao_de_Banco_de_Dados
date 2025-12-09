from repositories.activity import ActivityRepository
from models.activity import Activity
from bson import ObjectId

class ActivityService:
    def __init__(self, activity_repo, user_repo):
        self.activity_repo = activity_repo
        self.user_repo = user_repo

    def criar_atividade(self, data):
        user = self.user_repo.find_by_id(data["user_id"])
        if not user:
            raise Exception("Usuário não encontrado")
        return self.activity_repo.create(data)

    def listar(self):
        return self.activity_repo.list_all()

    def atualizar(self, activity_id, data):
        return self.activity_repo.update(activity_id, data)

    def remover(self, activity_id):
        return self.activity_repo.delete(activity_id)

    def atividades_em_andamento(self):
        return self.activity_repo.atividades_em_andamento_com_responsavel()

    def resumo_por_status(self):
        return self.activity_repo.quantidade_de_atividades_por_status()
