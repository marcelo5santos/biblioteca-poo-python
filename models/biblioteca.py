"""seção onde está a biblioteca, onde definimos a classe Biblioteca e seus métodos para gerenciar os livros. A classe Biblioteca tem um atributo para armazenar os livros e métodos para adicionar um livro e listar os livros disponíveis."""
from .livros import Livro 
from .usuarios import Usuario
class Biblioteca:
    def __init__(self):     
        self.livros = []
        self.__usuarios_cadastrados = []


    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível.")
        else:
            for livro in self.livros:
                print(livro)                                                                                        

    def cadastrar_usuario(self, usuario: Usuario):
        self.__usuarios_cadastrados.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso!")

    def listar_usuarios(self):
        if not self.__usuarios_cadastrados:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.__usuarios_cadastrados:
                print(f"- {usuario.nome}")
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