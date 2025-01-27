import sqlite3


def conectar_db(nome_db):
    conexao = sqlite3.connect(nome_db)
    return conexao

# Criando Tabela
def criar_tabela(conexao):
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

# Inserir dados em uma tabela
def inserir_funcionario(conexao, id, nome, cargo, dataContratacao):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Funcionarios VALUES (?, ?, ?, ?)",
                   (id, nome, cargo, dataContratacao))
    conexao.commit()

# Listar todos os dados da tabela
def selecionar_todos_funcionarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    return cursor.fetchall()

# Alterar dados de uma tabela
def atualizar_funcionario(conexao, id, cargo):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Funcionarios SET cargo = ? WHERE id = ?", (cargo, id))
    conexao.commit()

# Excluir dados de uma tebela
def deletar_funcionario(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Funcionarios WHERE id = ?", (id,))
    conexao.commit()

conexao = conectar_db('funcionarios.db')

criar_tabela(conexao)

nome = input('Digite seu nome: ')
cargo = input('Informe o cargo: ')
data = input('Digite a data no formato aaaa-mm-dd')

inserir_funcionario(conexao, 1, nome, cargo, data)
inserir_funcionario(conexao, 2, nome, cargo, data)

print(selecionar_todos_funcionarios(conexao))

atualizar_funcionario(conexao, 1, 'Desenvolvedor Sênior')

print(selecionar_todos_funcionarios(conexao))

deletar_funcionario(conexao, 1)

print(selecionar_todos_funcionarios(conexao))

conexao.close()

