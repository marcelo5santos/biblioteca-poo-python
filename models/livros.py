"""seção criação da entidade livro, onde definimos a classe Livro e seus atributos. Essa classe representa um livro na biblioteca, com atributos como título, autor e ano de publicação."""
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"
