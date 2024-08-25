from bases_scripts.bd_biblioteca import sqlite3, DB_FILE

def create_admin(usuario, senha):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    try:
        user = (f'INSERT INTO admin (user_name, senha)\
            VALUES (:user_name, :senha)')
    
        cursor.execute(user,
                   {
                       'user_name': usuario, 'senha': senha
                   }
        )
    except sqlite3.IntegrityError:
        print('Usuario ja existe!')
        # raise sqlite3.IntegrityError('Usuario já existe na base de dados!')
    
    finally:
        connection.commit()

    cursor.close()
    connection.close()


def login_admin(usuario, senha):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        'select * from admin'
    )

    user = cursor.fetchall()

    for linha in user:
        _id, name, senha_admin = linha
        
        if usuario == name and senha == senha_admin:
            print('Login Realizado!')
            break
        else:
            print('Usuario invalido!')
            break

    cursor.close()
    connection.close()
