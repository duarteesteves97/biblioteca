from io_terminal import imprime_lista

nome_ficheiro_lista_de_funcionarios = "lista_de_funcionarios.pk"

def imprime_lista_de_funcionarios(lista_de_funcionarios):

    '''Esta função vai imprimir uma lista de funcionáros

        Args:
            lista_de_funcionarios(list): Lista de fuincionarios

        Returns:
             List: Retorna uma lista de funcionarios
    '''

    imprime_lista(cabecalho="Lista de Funcionarios", lista=lista_de_funcionarios)

def cria_novo_funcionario():
    '''Pedir os dados de um novo funcionario

    :return: dicionario com o novo funcionario, {"nome": <<nome>>, "nif": <<nif>>, ...}
    '''
    pass
