"""Modulo principal do sistema de biblioteca.

Implementa o menu e a interface do usuário para interagir com a biblioteca.
"""

from models.biblioteca import Biblioteca
from utils.menu import Opcoes_livros, Opcoes_usuarios, Opcoes_da_biblioteca


def menu() -> None:
    """Executa o menu principal da biblioteca.
    
    Implementa um loop infinito com opções para gerenciar livros,
    usuários e visualizar informações da biblioteca.
    """
    biblioteca: Biblioteca = Biblioteca()
    
    while True:
        print("\n=== Menu ===")
        print("1. Gerenciar livros")
        print("2. Gerenciar usuários")
        print("3. Gerenciar biblioteca")
        print("4. Sair")
        
        opcao: str = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Seção de gerenciamento de livros
            while True:
                print("\n=== Opções de Livros ===")
                print("1. Adicionar livro")
                print("2. Listar livros")
                print("3. Voltar ao menu principal")
                opcao_livro: str = input("Escolha uma opção: ")
                
                if opcao_livro == "1":
                    opcoes_livros: Opcoes_livros = Opcoes_livros()
                    opcoes_livros.adicionar_livro(biblioteca)
                elif opcao_livro == "2":
                    biblioteca.listar_livros()
                elif opcao_livro == "3":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao == "2":
            # Seção de gerenciamento de usuários
            while True:
                print("\n=== Opções de Usuários ===")
                print("1. Cadastrar usuário")
                print("2. Listar usuários")
                print("3. Devolver livro")
                print("4. Voltar ao menu principal")
                opcao_usuario: str = input("Escolha uma opção: ")
                
                if opcao_usuario == "1":
                    opcoes_usuarios: Opcoes_usuarios = Opcoes_usuarios()
                    opcoes_usuarios.cadastrar_usuario(biblioteca)
                elif opcao_usuario == "2":
                    biblioteca.listar_usuarios()
                elif opcao_usuario == "3":
                    opcoes_usuarios = Opcoes_usuarios()
                    opcoes_usuarios.devolver_livro(biblioteca)

                elif opcao_usuario == "4":    
                    break
                else:
                    print("Opção inválida!")
            
        elif opcao == "3":
            # Seção de gerenciamento da biblioteca
            opcoes_biblioteca: Opcoes_da_biblioteca = Opcoes_da_biblioteca()
            opcoes_biblioteca.listar_livros_usuarios(biblioteca)
            
            while True:
                print("\n=== Opções de Biblioteca ===")
                print("1. Emprestar livro")
                print("2. Voltar ao menu principal")
                opcao_biblioteca: str = input("Escolha uma opção: ")
                
                if opcao_biblioteca == "1":
                    opcoes_biblioteca.emprestar_livro(biblioteca)
                elif opcao_biblioteca == "2":
                    break
                else:
                    print("Opção inválida!")
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()