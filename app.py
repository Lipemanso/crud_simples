# Arquivo principal da aplicação
# app.py
import operacoes_crud as crud  # Importamos o CRUD e damos um "apelido"
import banco_de_dados
import os

def limpar_tela():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    """Exibe o menu principal e gerencia a entrada do usuário."""
    
    # Garante que a tabela exista ANTES de mostrar o menu
    banco_de_dados.criar_tabela() 
    
    while True:
        limpar_tela()
        print("=" * 30)
        print("   SISTEMA DE CADASTRO")
        print("=" * 30)
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Sair")
        print("-" * 30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[Adicionar Produto]")
            nome = input("Nome: ")
            preco = float(input("Preço (ex: 19.99): "))
            estoque = int(input("Estoque: "))
            # Chama a função do outro módulo
            crud.adicionar_produto(nome, preco, estoque)
        
        elif opcao == '2':
            print("\n[Listar Produtos]")
            # Chama a função do outro módulo
            produtos = crud.listar_produtos() 
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print(f"{'ID':<5} | {'Nome':<20} | {'Preço':<10} | {'Estoque':<10}")
                print("-" * 55)
                for produto in produtos:
                    preco_formatado = f"R$ {produto[2]:.2f}"
                    print(f"{produto[0]:<5} | {produto[1]:<20} | {preco_formatado:<10} | {produto[3]:<10}")

        elif opcao == '3':
            print("\n[Atualizar Produto]")
            # Primeiro lista para o usuário ver os IDs
            menu_opcao_2() 
            try:
                id = int(input("Digite o ID do produto para atualizar: "))
                nome = input("Novo Nome: ")
                preco = float(input("Novo Preço: "))
                estoque = int(input("Novo Estoque: "))
                crud.atualizar_produto(id, nome, preco, estoque)
            except ValueError:
                print("Entrada inválida. IDs, preços e estoques devem ser números.")

        elif opcao == '4':
            print("\n[Remover Produto]")
            # Primeiro lista para o usuário ver os IDs
            menu_opcao_2()
            try:
                id = int(input("Digite o ID do produto para remover: "))
                crud.remover_produto(id)
            except ValueError:
                print("Entrada inválida. O ID deve ser um número.")

        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

# --- Ponto de Entrada Principal ---
# Garante que o menu() só rode quando este arquivo for executado diretamente
if __name__ == "__main__":
    menu()
