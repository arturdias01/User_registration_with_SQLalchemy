from configs.connection import session
from entities.users_table import Users


class UpdateUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.new_name = None
        self.new_age = None

    def set_name(self, new_name):
        self.new_name = new_name

    def set_age(self, new_age):
        self.new_age = new_age

    def process(self):
        option = input('[1] - confirmar  | [2] - cancelar: ')
        if option == '1':
            if self.new_name != '':
                self.__update_name()

            if self.new_age != '':
                self.__update_age()
        else:
            print('Operação cancelada.')


    def print_id(self):
        this_user = session.query(Users).filter_by(id=self.user_id).first()
        print(f'id: {this_user.id} | name: {this_user.name}, | age: {this_user.age}')

    def __update_name(self):
        user_to_update = session.query(Users).filter_by(id=self.user_id).first()
        user_to_update.name = self.new_name
        session.commit()

    def __update_age(self):
        user_to_update = session.query(Users).filter_by(id=self.user_id).first()
        user_to_update.age = self.new_age
        session.commit()
