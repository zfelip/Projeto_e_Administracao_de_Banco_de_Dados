from bson import ObjectId

class ActivityRepository:
    def __init__(self, db):
        self.collection = db["atividades"]

    def create(self, activity_data):
        return self.collection.insert_one(activity_data)

    def list_all(self):
        return list(self.collection.find())

    def get_by_id(self, activity_id):
        return self.collection.find_one({"_id": ObjectId(activity_id)})

    def update(self, activity_id, new_data):
        return self.collection.update_one(
            {"_id": ObjectId(activity_id)},
            {"$set": new_data}
        )

    def delete(self, activity_id):
        return self.collection.delete_one({"_id": ObjectId(activity_id)})

    def atividades_em_andamento_com_responsavel(self):
        pipeline = [
            {"$match": {"status": "andamento"}},
            {
                "$lookup": {
                    "from": "usuarios",
                    "localField": "user_id",
                    "foreignField": "_id",
                    "as": "responsavel"
                }
            },
            {"$unwind": "$responsavel"},
            {
                "$project": {
                    "title": 1,
                    "status": 1,
                    "responsavel": "$responsavel.name"
                }
            }
        ]

        return list(self.collection.aggregate(pipeline))

    def quantidade_de_atividades_por_status(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$status",
                    "total": {"$sum": 1}
                }
            },
            {"$sort": {"total": -1}}
        ]

        return list(self.collection.aggregate(pipeline))
