"""Modulo de interface do usuário (menu).

Implementa a interface de menu para interagir com a biblioteca.
O usuário pode escolher opções para adicionar livros, cadastrar usuários,
emprestar e devolver livros.
"""

from typing import Optional
from models.biblioteca import Biblioteca
from models.livros import Livro
from models.usuarios import Usuario


class Opcoes_livros:
    """Opções relacionadas ao gerenciamento de livros."""

    def adicionar_livro(self, biblioteca: Biblioteca) -> None:
        """Adiciona um novo livro à biblioteca através de entrada do usuário.
        
        Args:
            biblioteca: Instância da biblioteca
        """
        titulo: str = input("Digite o título do livro: ")
        autor: str = input("Digite o autor do livro: ")
        ano: int = int(input("Digite o ano de publicação: "))
        livro: Livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)


class Opcoes_usuarios:
    """Opções relacionadas ao gerenciamento de usuários."""

    def cadastrar_usuario(self, biblioteca: Biblioteca) -> None:
        """Cadastra um novo usuário na biblioteca através de entrada do usuário.
        
        Args:
            biblioteca: Instância da biblioteca
        """
        nome: str = input("Digite o nome do usuário: ")
        usuario: Usuario = Usuario(nome)
        biblioteca.cadastrar_usuario(usuario)

    def devolver_livro(self, biblioteca: Biblioteca) -> None:
        """Processa a devolução de um livro emprestado.
        
        Args:
            biblioteca: Instância da biblioteca
        """
        nome_usuario: str = input("Digite o nome do usuário: ")
        usuario: Optional[Usuario] = next(
            (u for u in biblioteca._Biblioteca__usuarios_cadastrados
             if u.nome == nome_usuario),
            None
        )
        if not usuario:
            print(f"Usuário '{nome_usuario}' não encontrado.")
            return
        
        titulo_livro: str = input("Digite o título do livro a ser devolvido: ")
        livro: Optional[Livro] = next(
            (livro_item for livro_item in usuario.livros_emprestados
             if livro_item.titulo == titulo_livro),
            None
        )
        if not livro:
            print(f"Livro '{titulo_livro}' não encontrado na lista de empréstimos do usuário '{usuario.nome}'.")
            return
        
        usuario.devolver_livro(livro=livro, biblioteca=biblioteca)
        biblioteca.adicionar_livro(livro)
        print(f"Livro '{livro.titulo}' devolvido por '{usuario.nome}'.")


class Opcoes_da_biblioteca:
    """Opções gerais da biblioteca."""

    def listar_livros_usuarios(self, biblioteca: Biblioteca) -> None:
        """Lista todos os livros e usuários da biblioteca.
        
        Args:
            biblioteca: Instância da biblioteca
        """
        print("\n=== Biblioteca ===")
        print("Livros disponíveis:")
        biblioteca.listar_livros()
        print("Usuários cadastrados:")
        biblioteca.listar_usuarios()

    def emprestar_livro(self, biblioteca: Biblioteca) -> None:
        """Processa o empréstimo de um livro para um usuário.
        
        Args:
            biblioteca: Instância da biblioteca
        """
        if not biblioteca.livros:
            print("Nenhum livro disponível para empréstimo.")
            return
        
        nome_usuario: str = input("Digite o nome do usuário: ")
        usuario: Optional[Usuario] = next(
            (u for u in biblioteca._Biblioteca__usuarios_cadastrados
             if u.nome == nome_usuario),
            None
        )
        if not usuario:
            print(f"Usuário '{nome_usuario}' não encontrado.")
            return
        
        titulo_livro: str = input("Digite o título do livro: ")
        livro: Optional[Livro] = next(
            (livro_item for livro_item in biblioteca.livros
             if livro_item.titulo == titulo_livro),
            None
        )
        if not livro:
            print(f"Livro '{titulo_livro}' não encontrado.")
            return
        
        usuario.pegar_emprestado(livro)
        biblioteca.livros.remove(livro)
        print(f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'.")