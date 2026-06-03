"""Modulo de gerenciamento de usuários.

Define a classe Usuario e seus métodos para gerenciar os usuários.
A classe Usuario armazena o nome do usuário e uma lista de livros emprestados,
além de métodos para emprestar e devolver livros.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .biblioteca import Biblioteca
    from .livros import Livro


class Usuario:
    """Representa um usuário da biblioteca.
    
    Atributos:
        nome: Nome do usuário
        livros_emprestados: Lista de livros emprestados pelo usuário
    """

    def __init__(self, nome: str) -> None:
        """Inicializa uma instância de Usuario.
        
        Args:
            nome: Nome do usuário
        """
        self.nome: str = nome
        self.livros_emprestados: list["Livro"] = []

    def pegar_emprestado(self, livro: "Livro") -> None:
        """Adiciona um livro à lista de livros emprestados.
        
        Args:
            livro: Livro a ser emprestado
        """
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro: "Livro", biblioteca: "Biblioteca") -> None:
        """Remove um livro da lista de emprestados e retorna à biblioteca.
        
        Args:
            livro: Livro a ser devolvido
            biblioteca: Instância da biblioteca
        """
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            biblioteca.livros.append(livro)