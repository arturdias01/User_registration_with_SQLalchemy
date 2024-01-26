from users_repository.insert import InsertIntoUsers
from users_repository.list import ListUsers
from configs.base import Base
from configs.connection import engine
from users_repository.delete import DeleteUser
from users_repository.update import UpdateUser

Base.metadata.create_all(engine)


def sep():
    print('\n -------------------------------------- \n')


menu = '''
[1] - cadastrar usuários;
[2] - editar usáario;
[3] - excluir usuário;
[4] - listar usuários;
[0] - Sair.
'''

while True:
    print(menu)
    option = input('>>> ')

    if option == '0':
        print('Encerrando...')
        break

    elif option == '1':
        try:
            name = input('Digite o nome do usuario: ')
            age = int(input('Digite a idade do usuario: '))
            new_user = InsertIntoUsers(name, age)
            print(new_user.__repr__())
            new_user.confirm()
        except ValueError as ve:
            print(ve)
            print(f'ERRO: O valor deve ser do tipo inteiro.')
        except NameError as ne:
            print(ne)
        sep()

    elif option == '2':
        try:
            user_id = int(input('Digite o id do usuario que pretende atualizar: '))
            update_user = UpdateUser(user_id)
            update_user.print_id()
            new_name = input('Novo nome(ou deixe em branco): ')
            new_age = input('Nova idade(ou deixe em branco): ')
            update_user.set_name(new_name)
            update_user.set_age(new_age)
            update_user.process()
        except ValueError as ve:
            print(ve)
            print(f'ERRO: O tipo de valor de alguma das entradas está incorreto.')
        sep()

    elif option == '3':
        try:
            user_id = int(input('Digite o id do usuario a ser deletado: '))
            user = DeleteUser(user_id)
            print('deseja deletar este usuário do banco de dados?')
            user.print_id()
            user.confirm()
        except ValueError as ve:
            print(ve)
            print(f'ERRO: O valor deve ser do tipo inteiro.')

        except AttributeError as ae:
            print(ae)
            print('ERRO: id não encontrado.')
        sep()

    elif option == '4':
        ListUsers.list()
        sep()

    else:
        print('Opção indisponivel')
        sep()
