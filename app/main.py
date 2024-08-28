from time import sleep

from classes import Biblioteca, Usuario, Emprestimo, Admin

biblioteca = Biblioteca('', '', '', None)
usuario = Usuario('', '', '', None, '', '', '')
emprestimo = Emprestimo(None, None, '', '')
admin = Admin('admin', 'admin')


def usuarios():
    user = input('Digite seu usuario: ')
    senha = input('Digite sua senha: ')

    teste =  usuario.login_user(user, senha)

    if teste == 'Login Realizado':
        print('Tudo certo\n')
        sleep(2)
        biblioteca.read_book()
        solicitar()

        
        
def solicitar():
    livro = input('Digite nome do livro: ')
    biblioteca.read_book(livro)

    emprestimos = input("Deseja fazer o emprestimo do livro: ")
    if emprestimos == 's':
        emprestimo.read_register()


def create_user():
    nome = input('Digite seu nome: ')
    username = input('Crie seu username: ')
    email = input('Digite seu email: ')
    senha = input('Crie um senha: ')
    rua = input('Digite sua rua: ')
    numero = input('Digite o numero: ')
    bairro = input('Digite o bairro: ')

    usuario = Usuario(nome, email, rua, numero, bairro, username, senha)
    usuario.add_user()
    usuario.create_user()


while True:
    print('Bem vindo a biblioteca!\n'.upper())
    print('Faça Login [1]/ Cadastre-se [2]')

    entrada = input('Digite a opção: ')

    match entrada:
        case '1':
            usuarios()
        case '2':
            create_user()



# def admin_biblioteca():
#     administrador = input('Você é Admin? [S]/[N]: ').lower()
    
#     if administrador == 's':
#         login_admin()


# def login_admin():
#     user = input('Digite seu usuario: ')
#     senha = input('Digite sua senha: ')

#     admin.login_admin(user, senha)

# admin_biblioteca()


    



# def livros():
#     while True:
#         print('Digite o numero da opção desejada:\n')
#         print('1-Adicionar')
