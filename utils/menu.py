"""seção voltada para o menu, onde criamos a interface do usuário para interagir com a biblioteca. Aqui, o usuário pode escolher opções para adicionar livros, listar livros, cadastrar usuários, listar usuários e emprestar livros. O menu é implementado em um loop infinito, permitindo que o usuário continue interagindo até escolher sair."""
from models.biblioteca import Biblioteca
from models.livros import Livro
from models.usuarios import Usuario
class Opcoes_livros:
    def adicionar_livro(self, biblioteca: Biblioteca):
        titulo: str = input("Digite o título do livro: ")
        autor: str = input("Digite o autor do livro: ")
        ano: int = int(input("Digite o ano de publicação: "))
        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)
class Opcoes_usuarios:
    def cadastrar_usuario(self, biblioteca: Biblioteca):
        nome: str = input("Digite o nome do usuário: ")
        usuario = Usuario(nome)
        biblioteca.cadastrar_usuario(usuario)
class Opcoes_da_biblioteca:
    def listar_livros_usuarios(self, biblioteca: Biblioteca):
        print("\n=== Biblioteca ===")
        print("Livros disponíveis:")
        biblioteca.listar_livros()
        print("Usuários cadastrados:")
        biblioteca.listar_usuarios()

    def emprestar_livro(self, biblioteca: Biblioteca):
        if not biblioteca.livros:
            print("Nenhum livro disponível para empréstimo.")
            return
        nome_usuario: str = input("Digite o nome do usuário: ")
        usuario = next((u for u in biblioteca._Biblioteca__usuarios_cadastrados if u.nome == nome_usuario), None)
        if not usuario:
            print(f"Usuário '{nome_usuario}' não encontrado.")
            return
        titulo_livro: str = input("Digite o título do livro: ")
        livro = next((livro_item for livro_item in biblioteca.livros if livro_item.titulo == titulo_livro), None)
        if not livro:
            print(f"Livro '{titulo_livro}' não encontrado.")
            return
        usuario.pegar_emprestado(livro)
        biblioteca.livros.remove(livro)
        print(f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'.")