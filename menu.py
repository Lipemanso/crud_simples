import operacoes_crud as crud  # Importamos o CRUD e damos um "apelido"

def adicionar():
     print("\n[Adicionar Produto]")
     nome = input("Nome: ")
     preco = float(input("Preço (ex: 19.99): "))
     estoque = int(input("Estoque: "))
     # Chama a função do outro módulo
     crud.adicionar_produto(nome, preco, estoque)

def listar():
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

def editar():
     print("\n[Atualizar Produto]")
     # Primeiro lista para o usuário ver os IDs
     listar()
     try:
          id = int(input("Digite o ID do produto para atualizar: "))
          nome = input("Novo Nome: ")
          preco = float(input("Novo Preço: "))
          estoque = int(input("Novo Estoque: "))
          crud.atualizar_produto(id, nome, preco, estoque)
     except ValueError:
          print("Entrada inválida. IDs, preços e estoques devem ser números.")
                

def remover():
     print("\n[Remover Produto]")
     # Primeiro lista para o usuário ver os IDs
     listar()
     try:
          id = int(input("Digite o ID do produto para remover: "))
          crud.remover_produto(id)
                
     except ValueError:
           print("Entrada inválida. O ID deve ser um número.")

def sair():
     print("Saindo...")
     
     
            
        
        


            

     
               
            
          