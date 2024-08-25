
from bases_scripts import admin
from bases_scripts import bd_biblioteca as bd
from bases_scripts import db_emprestimo as db
from bases_scripts import db_usuarios as db_u

class Biblioteca:
    def __init__(self, title, author, ano_published, quantity) -> None:
        self.title = title
        self.author = author
        self.ano_published = ano_published
        self.quantity = quantity

    def add_book(self):
        bd.add_books(self.title, self.author,self.ano_published, self.quantity)
    
    def read_book(self, title: str | None = None, author: str | None = None):
        if title is not None:
            bd.read_books(title)
            return
        if author is not None:
            bd.read_books(author)
            return
        bd.read_books()
    
    def edit_books(self, quantity: int, id: int):
        bd.edit_books(quantity, id)
    
    def remove_books(self, id):
        bd.remove_books(id)



class Usuario:
    def __init__(self, nome, email, rua, numero, bairro, username, senha) -> None:
        self.nome = nome
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.username = username
        self.senha = senha

    def add_user(self):
        db_u.add_user(self.nome, self.email, self.rua, self.numero, self.bairro)
    
    def read_user(self):
        db_u.read_users()
    
    def edit_user(self, id, email, rua, numero, bairro):
        db_u.edit_user(id, email, rua, numero, bairro)
    
    def remove_user(self, id):
        db_u.remove_user(id)
    
    def login_user(self, usuario, senha):
        db_u.login_user(usuario, senha)
    
    def create_user(self, id_user, username, senha):
        db_u.create_user(id_user, username, senha)



class Emprestimo:
    def __init__(self, id_usuario, id_livro, data_devolucao, devolvido) -> None:
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.data_devolucao = data_devolucao
        self.devolvido = devolvido
    
    def register(self):
        db.register(self.id_usuario, self.id_livro, self.data_devolucao, self.devolvido)

    def read_emprestimo(self):
        db.read_emprestimo()

    def read_register(self):
        db.read_register()

    def mark_returned(self,id_livro, devolvido):
        db.mark_returned(id_livro, devolvido)
    
    def open_loan(self):
        db.open_loan()
    
    def remove_emprestomo(self, id):
        db.remove_emprestimo(id)

class Admin:
    def __init__(self, usuario, senha) -> None:
        self.usuario = usuario
        self.senha = senha
    
    def create_admin(self):
        admin.create_admin(self.usuario, self.senha)
    
    def login_admin(self, user, password):
        admin.login_admin(user, password)
