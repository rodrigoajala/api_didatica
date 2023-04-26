import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)  # instanciar o Flask com essa variavel.( foi usado
# dunder name porque assume o nome do modulo do arquivo).

# books = [
#     {
#         'id': 1,
#         'title': 'Trabahe 4 horas por semana',
#         'author': 'Timothy Ferriss'
#     },
#     {
#         'id': 2,
#         'title': 'Como Fazer amigos e influenciar pessoas',
#         'author': 'Dale Carnegie'
#     },
#     {
#         'id': 3,
#         'title': 'Quem pensa Enrriquece',
#         'author': 'Napoleon Hill'
#     },
# ]


# Consultar todos (todos)


@app.route('/books', methods=['GET'])  # @ decorator do pacote Flask
# para indicar a rota que essa função executara o tipo e o verbo.
def Consult_books():
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM livros')
    return jsonify(result.fetchall())


# Consultar (id)

@app.route('/books/<int:id>', methods=['GET'])
def search_id(id):
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()
    result = cursor.execute(
        'SELECT * FROM livros WHERE id = :id', {"id": id})
    return jsonify(result.fetchone())

# Editar


@app.route('/books/<int:id>', methods=['PUT'])
def edit_books(id):
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()
    book_changed = request.get_json()
    book_changed['id'] = id
    cursor.execute(
        'UPDATE livros SET title= :title, author= :author  WHERE id= :id', book_changed)
    connection.commit()
    return jsonify(book_changed)


# Criar

@app.route('/books', methods=['POST'])
def include_book():
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()
    new_book = request.get_json()  # get_jason pegar todos os dados da requisição
    # do usuario para a variavel de objeto da linguagem (python neste caso).
    cursor.execute('INSERT INTO livros VALUES(:id, :title, :author)', new_book)
    connection.commit()
    return jsonify(new_book)


# Excluir

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    connection = sqlite3.connect('BOOKS.db')
    cursor = connection.cursor()
    cursor.execute(
        ' DELETE FROM livros WHERE id = :id', {"id": id})
    connection.commit()
    return jsonify({"msg": 'Livro deletado com sucesso!!'})


app.run(port=5000, host='localhost', debug=True)  # para disponibilizar a
# API para ser acessada foi usado o comando "run"
