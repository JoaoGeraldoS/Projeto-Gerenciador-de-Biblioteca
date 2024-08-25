from bases_scripts.bd_biblioteca import DB_FILE, sqlite3


def add_user(nome, email,username, senha, rua: str | None = None, numero: int | None = None, bairro: str | None = None):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = (f'INSERT INTO usuarios (nome, email, rua, numero, bairro)'
                f'VALUES (:nome, :email, :username, :senha, :rua, :numero, :bairro)')
    
    
    
    connection.execute(
        valor,
        {
            'nome': nome, 'email': email, 'username': username, 'senha':senha, 'rua': rua, 'numero': numero, 'bairro': bairro
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
        'select * from login_user'
    )

    user = cursor.fetchall()

    for linha in user:
        _id,id_usuario, name, senha_user = linha
        
        if usuario == name and senha == senha_user:
            print('Login Realizado!')
            break
        else:
            print('Usuario invalido!')
            break

    cursor.close()
    connection.close()

def create_user(id_user, usuario, senha):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = (f'INSERT INTO login_user (id_usuario, username, senha)\
             VALUES(:id_usuario, :username, :senha)')
    
    cursor.execute(valor,
                   {
                        'id_usuario': id_user, 'username': usuario, 'senha': senha
                   }
    )
    connection.commit()

    cursor.close()
    connection.close()

