from .bd_biblioteca import DB_FILE, sqlite3


def add_user(nome, username, email, senha, rua: str | None = None, numero: int | None = None, bairro: str | None = None):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = (f'INSERT INTO usuarios (nome, email, rua, numero, bairro, username, senha)'
                f'VALUES (:nome, :email, :rua, :numero, :bairro, :username, :senha)')
    

    connection.execute(
        valor,
        {
            'nome': nome, 'username': username, 'email':email , 'senha': senha, 'rua':rua, 'numero':numero, 'bairro': bairro
        }
    )
    connection.commit()

    cursor.close()
    connection.close()

def read_users():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM usuarios')

    usuarios = cursor.fetchall()
    
    for linha in usuarios:
        _id, nome, email, rua, numero, bairro = linha
        print(f'Id: {_id}\nNome: {nome}\nEmail: {email}\nRua: {rua}\nNumero: {numero}\nBairro: {bairro}\n')

    cursor.close()
    connection.close()


def edit_user(id, email, rua, numero, bairro):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'UPDATE usuarios SET email={email}, rua={rua}, numero={numero}, bairro={bairro} WHERE id_usuario= "{id}"'
    )
    connection.commit()

    cursor.close()
    connection.close()


def remove_user(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'DELETE FROM usuarios WHERE id_usuario = "{id}" '
    )
    cursor.execute(
        f'DELETE FROM emprestimo WHERE id_usuario = "{id}" '
    )
    connection.commit()

    cursor.close()
    connection.close()


def login_user(usuario, senha):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'select * from login_user where username = "{usuario}" and senha = "{senha}"'
    )

    user = cursor.fetchall()

    if len(user) == 0: 
        print('Usuario e Senha invalidos ou inexistentes') 
        return
    

    for linha in user:
        _id,id_usuario, name, senha_user = linha
        
        if name and senha_user:
            print('Login Realizado!')
            return 'Login Realizado'
            
        

    cursor.close()
    connection.close()

def create_user():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = ('INSERT into login_user (id_usuario ,username, senha)\
        select id_usuario, username, senha from usuarios WHERE id_usuario = id_usuario ORDER BY id_usuario DESC LIMIT 1')
    
    cursor.execute(valor)
    connection.commit()

    cursor.close()
    connection.close()

