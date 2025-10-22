# Operações de CRUD - criar, ler, editar e deletar.
import sqlite3
import banco_de_dados  # Importa nosso módulo de banco de dados

def adicionar_produto(nome, preco, estoque):
    """Adiciona um novo produto ao banco de dados."""
    conexao = banco_de_dados.conectar()
    if conexao is None:
        return
        
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
                       (nome, preco, estoque))
        conexao.commit()
        print(f"Produto '{nome}' adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao adicionar o produto: {e}")
    finally:
        if conexao:
            conexao.close()

def listar_produtos():
    """Retorna uma lista de todos os produtos cadastrados."""
    conexao = banco_de_dados.conectar()
    if conexao is None:
        return []
        
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        return produtos
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao listar os produtos: {e}")
        return [] # Retorna lista vazia em caso de erro
    finally:
        if conexao:
            conexao.close()

def atualizar_produto(id, novo_nome, novo_preco, novo_estoque):
    """Atualiza um produto existente com base no ID."""
    conexao = banco_de_dados.conectar()
    if conexao is None:
        return
        
    try:
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE produtos 
        SET nome = ?, preco = ?, estoque = ? 
        WHERE id = ?
        """, (novo_nome, novo_preco, novo_estoque, id))
        
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"Produto ID {id} atualizado com sucesso!")
        else:
            print(f"Nenhum produto encontrado com o ID {id}.")
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao atualizar o produto: {e}")
    finally:
        if conexao:
            conexao.close()

def remover_produto(id):
    """Remove um produto do banco de dados com base no ID."""
    conexao = banco_de_dados.conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Produto ID {id} removido com sucesso!")
        else:
            print(f"Nenhum produto encontrado com o ID {id}.")
    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao remover o produto: {e}")
    finally:
        if conexao:
            conexao.close()