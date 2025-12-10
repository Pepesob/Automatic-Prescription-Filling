from enum import Enum
from dataclasses import dataclass, asdict
import os
import json


class Branch(Enum):
    LUBELSKIE = "Lubelski (03)"

@dataclass
class User:
    login: str
    password: str
    branch: Branch
    seed_2fa: str


class UserService:

    def __init__(self):
        self.data_path: str = os.path.join(os.path.dirname(__file__), "resources", "data.json") 

    def add_user(self, user: User):
        users = self._read_data_file()
        users.append(user)
        self._write_data_file(users)

    def edit_user(self, user: User):
        users = self._read_data_file()
        new_users = [old_user if old_user.login != user.login else user for old_user in users]
        self._write_data_file(new_users)
    
    def delete_user(self, login: str):
        users = self._read_data_file()
        users_new = [user for user in users if user.login != login]
        self._write_data_file(users_new)

    def get_by_login(self, login)-> User | None:
        users = self._read_data_file()
        for user in users:
            if user.login == login:
                return user
        return None

    def get_all_users(self) -> list[User]:
        return self._read_data_file()

    # TODO - add validation so two users cannot have the same login
    def _read_data_file(self) -> list[User]:
        with open(self.data_path, encoding="utf-8") as f:
            dict_data = json.load(f)
            users = []
            for d in dict_data:
                users.append(User(**d))
            return users
    
    def _write_data_file(self, users: list[User]):
        with open(self.data_path, "w", encoding="utf-8") as f:
            dict_data = []
            for user in users:
                dict_data.append(asdict(user))
            json.dump(dict_data, f, indent=4)
