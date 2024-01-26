from configs.connection import session
from entities.users_table import Users


class ListUsers:
    @classmethod
    def list(cls):
        all_users = session.query(Users).all()
        for user in all_users:
            print(f'id: {user.id} | name: {user.name}, | age: {user.age}')
