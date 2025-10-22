# Criação e conexão com o banco sqlite3

import sqlite3

DB_FILE = 'cadastro.db'

def conectar():
    """Conecta ao banco de dados SQLite."""
    try:
        conexao = sqlite3.connect(DB_FILE)
        return conexao
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao conectar ao banco: {e}")
        return None

def criar_tabela():
    """Cria a tabela 'produtos' se ela ainda não existir."""
    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
        ''')
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao criar a tabela: {e}")
    finally:
        if conexao:
            conexao.close()