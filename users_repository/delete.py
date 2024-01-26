from configs.connection import session
from entities.users_table import Users

class DeleteUser:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'name: {self.name} / age: {self.age}.'

    def __delete(self):
        user_to_delete = session.query(Users).filter_by(id=self.user_id).first()
        session.delete(user_to_delete)
        session.commit()

    def print_id(self):
        this_user = session.query(Users).filter_by(id=self.user_id).first()
        print(f'id: {this_user.id} | name: {this_user.name}, | age: {this_user.age}')


    def confirm(self):
        option = input('[1] - confirmar  | [2] - cancelar: ')
        if option == '1':
            self.__delete()
            print('Usuário deletado.')
        else:
            print('Operação cancelada.')

