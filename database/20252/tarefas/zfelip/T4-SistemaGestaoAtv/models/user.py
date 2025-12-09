from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
