"""Modulo de criação da entidade livro.

Define a classe Livro e seus atributos. Essa classe representa um livro
na biblioteca, com atributos como título, autor e ano de publicação.
"""


class Livro:
    """Representa um livro na biblioteca.
    
    Atributos:
        titulo: Nome do livro
        autor: Autor do livro
        ano: Ano de publicação
    """

    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        """Inicializa uma instância de Livro.
        
        Args:
            titulo: Nome do livro
            autor: Autor do livro
            ano: Ano de publicação do livro
        """
        self.titulo: str = titulo
        self.autor: str = autor
        self.ano: int = ano

    def __str__(self) -> str:
        """Retorna uma representação em string do livro.
        
        Returns:
            String formatada com informações do livro
        """
        return f"{self.titulo} - {self.autor} ({self.ano})"
