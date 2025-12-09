from services.user import UserService

class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def create(self, name, email):
        return self.user_service.create_user(name, email)

