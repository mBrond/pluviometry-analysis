import csv
import os

def get_all_files(directory):
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

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
codigos = pegar_estacoes(path_estacoes, tipo_estacoes)

dirSource = 'Dados-Brutos/INMET/'
dirEnd = 'Dados-Separados/INMET/'
arquivos = get_all_files(dirSource)

arquivosSeparados = [arq for arq in arquivos if any(codigo in arq for codigo in codigos)]

for arq in arquivosSeparados:
    os.rename(dirSource+arq, dirEnd+arq)

