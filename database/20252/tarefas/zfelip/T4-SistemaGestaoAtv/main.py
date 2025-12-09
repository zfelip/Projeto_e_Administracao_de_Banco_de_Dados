from config.database import get_db
from repositories.user import UserRepository
from repositories.activity import ActivityRepository
from services.activity import ActivityService
from controllers.activity import ActivityController
from bson import ObjectId

db = get_db()

user_repo = UserRepository(db)
activity_repo = ActivityRepository(db)

service = ActivityService(activity_repo, user_repo)
controller = ActivityController(service)


print("\n-------------- Criando usuário --------------")
user_id = user_repo.create({
    "name": "Felipe",
    "email": "felipe@example.com"
}).inserted_id
print("ID usuário:", user_id)

print("\n-------------- Criando atividade --------------")
atividade_id = controller.criar({
    "title": "Atividade de Banco de Dados",
    "description": "Usar mongo + Python",
    "status": "andamento",
    "user_id": ObjectId(user_id)
}).inserted_id
print("ID atividade:", atividade_id)

print("\n-------------- Listar atividades --------------")
print(controller.listar())

print("\n-------------- Consulta complexa 1 --------------")
print(controller.andamento_com_responsavel())

print("\n-------------- Consulta complexa 2 --------------")
print(controller.resumo_status())
