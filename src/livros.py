from io_terminal import imprime_lista

nome_ficheiro_lista_de_livros = "lista_de_livros.pk"


def imprime_lista_de_livros(lista_de_livros):
    '''Esta função vai imprimir uma lista de livros

    Args:
        lista_de_livros(list): Lista de Livros

    Returns:
         List: Retorna uma lista de livros
    '''


imprime_lista(cabecalho="Lista de Livros", lista=lista_de_livros)


def cria_novo_livro():
    '''Pede ao utilizador para introduzir um novo livro

    :return: dicionario com um livro na forma
        {"titulo": <<titulo>>, "autor": <<autor>>, ...}
    '''

    titulo = input("titulo? ").title()
    autor = input("autor? ").title()

    livro = {
        "titulo": titulo,
        "autor": autor,
    }

    return livro