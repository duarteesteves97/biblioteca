from tabulate import tabulate

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_terminal*.py na pasta temp e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_terminal.py existente, deve apagar
# todos os outros ficheiros temp/io_terminal-*.py, e inclusive estes comentários

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

    def imprime_lista(cabecalho, lista):
        """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

        Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
        {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
        na forma

        ==  ======  ======
        id  atrib1  atrib2
        ==  ======  ======
        0   valor1  valor2
        1   ...      ...
        ==  ======  ======

        :param cabecalho: Cabecalho para a listagem
        :param lista: Lista a ser impressa
        """

        print(cabecalho)

        if (len(lista) == 0):
            print("Lista vazia")
        else:
            # cabecalho da tabela
            lista_a_imprimir = [["id"] + list(lista[0].keys())]
            # dados
            lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

            print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))
def pausa():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
        """

        :param questao:
        :param lista:
        :param mostra_lista:
        :return:
        """

        if mostra_lista:
            imprime_lista(cabecalho="", lista=lista)

        while True:
            id = int(input(questao))
            if 0 <= id < len(lista):
                return id
            else:
                print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
