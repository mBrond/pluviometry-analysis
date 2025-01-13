import csv
import os
import pandas as pd

def pegar_estacoes(path_estacoes:str, tipo_estacoes:str) ->list:
    """Lê o arquivo .csv com o código de todas as estações, e retorna apenas aquelas do tipo especificado
    
    Args:
        path_estacoes (str): Path para o arquivo .csv
        tipo_estacoes (str): Valor de acordo com a coluna "tipo" do .csv

    Returns:
        list: Lista com os códigos das estações do mesmo tipo de tipo_estacoes
    """
    codigos = list()

    with open(path_estacoes) as file:
        spamreader = csv.reader(file, delimiter=';')
        codigos = [cod[2] for cod in spamreader if tipo_estacoes in cod[1] ]        

    return codigos

def get_all_files(directory):
    """Retorna apenas os arquivos no diretorio

    Args:
        directory (_type_): Diretorio

    Returns:
        list: Lista com os arquivos
    """
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def apagar_nao_csv(pathArquivos): #REMOVE ARQUIVOS QUE NAO SAO .csv ? conferir se nome da func corresponde a sua funcao
    """Remove todos os arquivos que n

    Args:
        pathArquivos (_type_): _description_
    """
    arquivosCsv =  [arquivo for arquivo in os.listdir(pathArquivos) if '.csv' in arquivo]
    for arquivo in arquivosCsv:
        os.remove(f'{pathArquivos}//{arquivo}')

def converter_csv_para_xls(pathArquivos)->None:
    """Cria uma cópia .xls para cada arquivo .csv no diretório

    Args:
        pathArquivos (str): Path para diretório com os arquivos
    """
    for fileName in get_all_files(pathArquivos):
        df = pd.read_csv(f'{pathArquivos}\\{fileName}', encoding='latin-1')
        excelNome = f'{pathArquivos}\\{fileName[:-4]}.xlsx'
        df.to_excel(excelNome ,index=False)

def converter_csv_para_xls_externo(pathOrigem:str, pathFinal:str)->None:
    """Para cada arquivo .csv no diretório de pathOrigem, cria um arquivo .xls no diretório de pathFinal

    Args:
        pathOrigem (str): _description_
        pathFinal (str): _description_
    """
    for fileName in get_all_files(pathOrigem):
        df = pd.read_csv(f'{pathOrigem}\\{fileName}', encoding='latin-1', on_bad_lines='skip')
        excelNome = f'{pathFinal}\\{fileName[:-4]}.xlsx'
        df.to_excel(excelNome ,index=False)

def criar_pastas(pathBrutos, pathProcessados):
    """Cria as pastas que serão utilizadas no decorrer do código
    """
    pass

    #Dados-Brutos\\CEMADEN
    #Dados-Brutos\\INMET
    #Dados-Processados\\ANA
    #Dados-Processados\\CEMADEN
    #Dados-Processados\\INMET
    #Dados-Processados\\INMET\\csv
    #Dados-Processados\\INMET\\xls