from configs.connection import session
from entities.users_table import Users


class InsertIntoUsers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __insert(self):
        new_user = Users(name=self.name, age=self.age)
        session.add(new_user)
        session.commit()

    def __repr__(self):
        return f'name: {self.name} / age: {self.age}.'

    def confirm(self):
        option = input('[1] - confirmar inserção | [2] - cancelar inserção: ')
        if option == '1':
            self.__insert()
            print('Usuário cadastrado com sucesso.')
        else:
            print('Cadastro cancelado.')
