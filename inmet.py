import csv

def pegar_estacoes(path_estacoes:str, tipo_estacoes:str) ->list:
    """
    Args:
        path_estacoes (str): _description_
        tipo_estacoes (str): _description_

    Returns:
        list: Lista com os códigos das estações do mesmo tipo de tipo_estacoes
    """
    codigos = list()

    with open(path_estacoes) as file:
        spamreader = csv.reader(file, delimiter=';')
        codigos = [cod[2] for cod in spamreader if tipo_estacoes in cod[1] ]        


    return codigos

path_estacoes = 'estacoes.csv'
tipo_estacoes = 'INMET'
a = pegar_estacoes(path_estacoes, tipo_estacoes)
print(a)