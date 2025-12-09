from repositories.user import UserRepository
from models.user import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, name, email):
        user = User(name=name, email=email)
        return self.user_repository.create(user.__dict__)

