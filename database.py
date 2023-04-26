import sqlite3

connection = sqlite3.connect('BOOKS.db')
cursor = connection.cursor()


def creat_table():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS  livros ( id number, title text, author text )')


creat_table()


def dataentry():
    cursor.execute(
        'INSERT INTO livros VALUES(1, "Trabahe 4 horas por semana", "Timothy Ferriss")')
    cursor.execute(
        'INSERT INTO livros VALUES(2, "Como Fazer amigos e influenciar pessoas", "Dale Carnegie")')
    cursor.execute(
        'INSERT INTO livros VALUES(3, "Quem pensa Enrriquece", "Napoleon Hill")')
    connection.commit()


dataentry()
