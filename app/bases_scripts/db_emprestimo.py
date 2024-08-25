from bases_scripts.bd_biblioteca import DB_FILE, sqlite3


def register(id_usuario, id_livro, data_devolucao, devolvido):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = (f'INSERT INTO emprestimo (id_usuario, id_livro, data_devolucao, devolvido)'
                f'VALUES (:id_usuario, :id_livro, :data_devolucao, :devolvido)')
    
    connection.execute(
        valor,
        {
            'id_usuario': id_usuario, 'id_livro': id_livro, 'data_devolucao': data_devolucao, 'devolvido': devolvido
        }
    )
    connection.commit()

    cursor.close()
    connection.close()

def read_emprestimo():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM emprestimo')

    usuarios = cursor.fetchall()
    
    for linha in usuarios:
        _id, id_usuario, id_livro, data_devolucao, devolvido = linha
        print(f'Id: {_id}\nId_usuario: {id_usuario}\nId_livro: {id_livro}\nData devolução: {data_devolucao}\nDevolvido: {devolvido}\n')

    cursor.close()
    connection.close()

def read_register():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f'SELECT e.id_emprestimo, u.nome, l.title, e.data_devolucao, e.devolvido FROM usuarios u join emprestimo e on e.id_usuario = u.id_usuario\
                   join livros l on e.id_livro = l.id_livro')

    registro = cursor.fetchall()
    
    for linha in registro:
        _id, nome, title, data_devolucao, devolvido = linha
        print(f'Id: {_id}\nUsuario: {nome}\nLivro: {title}\nData devolução: {data_devolucao}\nDevolvido: {devolvido}\n')

    cursor.close()
    connection.close()

def mark_returned(id_livro: int, devolvido: str ):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'UPDATE emprestimo set devolvido="{devolvido}" WHERE id_livro ="{id_livro}"'
    )
    connection.commit()

    cursor.close()
    connection.close()


def open_loan():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'SELECT e.*, u.nome, l.title FROM usuarios u join emprestimo e\
              ON e.id_usuario = u.id_usuario JOIN Livros l\
                  ON e.id_livro = l.id_livro WHERE e.devolvido = "Não";'
    )

    devolvido = cursor.fetchall()

    for linha in devolvido:
        _id,id_usuario, id_livro, data, devolvidos, nome, title = linha
        print(f'Livro: {title}\nUsuario: {nome}\nDevolvido: {devolvidos}\n')
    
    cursor.close()
    connection.close()


def remove_emprestimo(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'DELETE FROM emprestimo WHERE id_emprestimo = "{id}"'
    )
    connection.commit()


    cursor.close()
    connection.close()