"""Modulo da classe Biblioteca.

Define a classe Biblioteca e seus métodos para gerenciar os livros e usuários.
A classe Biblioteca armazena os livros e usuários cadastrados, com métodos
para gerenciar empréstimos e devoluções.
"""

from .livros import Livro
from .usuarios import Usuario


class Biblioteca:
    """Representa a biblioteca do sistema.
    
    Atributos:
        livros: Lista de livros disponíveis
        __usuarios_cadastrados: Lista de usuários cadastrados (privada)
    """

    def __init__(self) -> None:
        """Inicializa uma instância de Biblioteca."""
        self.livros: list[Livro] = []
        self.__usuarios_cadastrados: list[Usuario] = []

    def adicionar_livro(self, livro: Livro) -> None:
        """Adiciona um livro à biblioteca.
        
        Args:
            livro: Livro a ser adicionado
        """
        self.livros.append(livro)

    def listar_livros(self) -> None:
        """Lista todos os livros disponíveis na biblioteca."""
        if not self.livros:
            print("Nenhum livro disponível.")
        else:
            for livro in self.livros:
                print(livro)

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        """Cadastra um novo usuário na biblioteca.
        
        Args:
            usuario: Usuario a ser cadastrado
        """
        self.__usuarios_cadastrados.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso!")

    def listar_usuarios(self) -> None:
        """Lista todos os usuários cadastrados na biblioteca."""
        if not self.__usuarios_cadastrados:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.__usuarios_cadastrados:
                print(f"- {usuario.nome}")

    def buscar_livro(self, titulo: str) -> str:
        """Busca um livro pelo título.
        
        Args:
            titulo: Título do livro a buscar
            
        Returns:
            Mensagem com resultado da busca
        """
        for livro in self.livros:
            if livro.titulo == titulo:
                return f"Esse livro está disponível na biblioteca: {livro}"
        return f'Livro "{titulo}" não encontrado na biblioteca.'

if __name__ == "__main__":
    """ Teste da classe Biblioteca, onde criamos uma instância da biblioteca, adicionamos alguns livros e usuários, e listamos os livros e usuários para verificar se tudo está funcionando corretamente."""
    # biblioteca = Biblioteca()
    # livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    # livro2 = Livro("1984", "George Orwell", 1949)
    # biblioteca.adicionar_livro(livro1)
    # biblioteca.adicionar_livro(livro2)
    # biblioteca.listar_livros()
    # usuario1 = Usuario("Alice")
    # usuario2 = Usuario("Bob")
    # biblioteca.cadastrar_usuario(usuario1)
    # biblioteca.cadastrar_usuario(usuario2)
    # biblioteca.listar_usuarios()