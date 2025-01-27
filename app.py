import sqlite3

conexao = sqlite3.connect('funcionarios.db')

cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        dataContratacao TEXT NOT NULL
    );
""")
conexao.commit()
