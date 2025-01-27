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

nome = input('Digite seu nome: ')
cargo = input('Digite um cargo: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')

cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",
               (1, nome, cargo, data))
conexao.commit()


nome = input('Digite seu nome: ')
cargo = input('Digite um cargo: ')
data = input('Digite uma data no formato aaaa-mm-dd: ')
cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",
               (2, nome, cargo, data))
conexao.commit()
