from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://root:root@localhost:27017/")
    db = client["gestao_atividades"]
    return db
