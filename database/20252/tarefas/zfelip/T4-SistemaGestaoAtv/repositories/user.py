from bson import ObjectId

class UserRepository:
    def __init__(self, db):
        self.collection = db["usuarios"]

    def create(self, user_data):
        return self.collection.insert_one(user_data)

    def find_by_id(self, user_id):
        return self.collection.find_one({"_id": user_id})

