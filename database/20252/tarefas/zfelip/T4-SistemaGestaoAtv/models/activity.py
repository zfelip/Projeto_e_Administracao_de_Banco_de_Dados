from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId

@dataclass
class Activity:
    def __init__(self, title, description, status, user_id):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id
