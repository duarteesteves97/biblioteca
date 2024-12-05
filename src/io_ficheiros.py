import pickle

from emprestimos import nome_ficheiro_lista_de_emprestimos
from funcionarios import nome_ficheiro_lista_de_funcionarios
from leitores import nome_ficheiro_lista_de_leitores
from livros import nome_ficheiro_lista_de_livros

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_ficheiros*.py na pasta temp e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_ficheiros.py existente, deve apagar
# todos os outros ficheiros temp/io_ficheiros-*.py, e inclusive estes comentários

# ...
def carrega_as_listas_dos_ficheiros():
    """
    Esta função carrega as listas dos ficheiros

    Return: lista de livros, lista de leitores, lista de emprestimos e lista de funcionrios
    """

    lista_de_livros = le_de_ficheiro(nome_ficheiro_lista_de_livros)
    lista_de_leitores = le_de_ficheiro(nome_ficheiro_lista_de_leitores)
    lista_de_emprestimos = le_de_ficheiro(nome_ficheiro_lista_de_emprestimos)
    lista_de_funcionarios = le_de_ficheiro(nome_ficheiro_lista_de_funcionarios)

    return  lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios

def guarda_as_listas_em_ficheiros(lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios):
    """
    guarda as listas em ficheiros

    :param lista_de_livros:
    :param lista_de_leitores:
    :param lista_de_emprestimos:
    :param lista_de_funcionarios:
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_livros, lista_de_livros)
        guarda_em_ficheiro(nome_ficheiro_lista_de_leitores, lista_de_leitores)
        guarda_em_ficheiro(nome_ficheiro_lista_de_emprestimos, lista_de_emprestimos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_funcionarios, lista_de_funcionarios)
    else:
        print("Gravação cancelada...")

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def le_de_ficheiro(nome_ficheiro):
    """Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    try:
        with open(nome_ficheiro, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"O ficheiro {nome_ficheiro} não existe.")
        return []