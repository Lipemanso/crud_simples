# Arquivo principal da aplicação
# app.py
import operacoes_crud as crud  # Importamos o CRUD e damos um "apelido"
import menu as funcoes
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
        funcoes.opcoes()
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            funcoes.adicionar()
           
        elif opcao == '2':
            funcoes.listar()

        elif opcao == '3':
            funcoes.editar()

        elif opcao == '4':
            funcoes.remover()

        elif opcao == '5':
            funcoes.sair()
            break
        
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

# --- Ponto de Entrada Principal ---
# Garante que o menu() só rode quando este arquivo for executado diretamente
if __name__ == "__main__":
    menu()
