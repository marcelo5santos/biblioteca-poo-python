"""Modulo usuarios onde definimos a classe Usuario e seus métodos para gerenciar os usuários. A classe Usuario tem atributos para armazenar o nome do usuário e uma lista de livros emprestados, além de métodos para emprestar um livro e devolver um livro."""
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)