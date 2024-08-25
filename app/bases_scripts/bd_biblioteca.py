import sqlite3
from pathlib import Path

ROOT_DIR  = Path(__file__).parent
DB_NAME = 'biblioteca_db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME


def add_books(title: str, author: str, ano_published: str, quantity: int):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    valor = (f'INSERT INTO Livros (title, author, ano_published, quantity)'
                f'VALUES (:title, :author, :ano_published, :quantity)')
    
    connection.execute(
        valor,
        {
            'title': title, 'author': author, 'ano_published':ano_published, 'quantity': quantity
        }
    )
    connection.commit()

    cursor.close()
    connection.close()



def read_books(title: str | None = None, author: str | None = None):

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    if title is not None:
        cursor.execute(f'SELECT * FROM Livros WHERE title = "{title}"')
        livros = cursor.fetchall()
        print(livros)
        return
    
    if author is not None:
        cursor.execute(f'SELECT * FROM Livros WHERE author = "{author}"')
        livros = cursor.fetchall()
        
        for linha in livros:
            print(linha)
        return

    cursor.execute(f'SELECT * FROM Livros')

    livros = cursor.fetchall()
    
    for linha in livros:
        _id, titulo, autor, ano, quantidade = linha
        print(f'Id: {_id}\nTitulo: {titulo}\nAutor: {autor}\nAno: {ano}\nQuantidade: {quantidade}\n')

    cursor.close()
    connection.close()


def edit_books(quantity, id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'UPDATE Livros SET quantity={quantity} WHERE id_livro = "{id}"'
    )
    connection.commit()


    cursor.close()
    connection.close()


def remove_books(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'DELETE FROM Livros WHERE id_livro = "{id}"'
    )
    cursor.execute(
        f'DELETE FROM emprestimo WHERE id_livro = "{id}"'
    )
    connection.commit()

    cursor.close()
    connection.close()
