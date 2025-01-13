import csv
import os

def copiar_header_CEMADEN(spamreader, arquivoFinal)->None:
    """Copia o header de um arquivo csv em outro

    Args:
        spamreader (_type_): Dados do csv
        arquivoFinal (_type_): Arquivo onde o header será escrito
    """
    for row in spamreader:
        for item in row:
            arquivoFinal.write(item+';')
        break
    arquivoFinal.write('\n')

def pega_nome(spamreader)->str:
    """Retorna o nome do município disponível no arquivo

    Args:
        spamreader (_type_): Dados do csv

    Returns:
        str: nome do município dos dados
    """
    linha2 = False
    for line in spamreader:
        if linha2:
            return line[0]
        linha2= True

def pega_mes_ano(spamreader)->str:
    """Retorna o mes e ano das medicoes contidas no arquivo do cemaden

    Args:
        spamreader (_type_): Dados do csv

    Returns:
        str: ano e número dos dados no formato (YYYY-MM) 
    """
    linha2 = False
    for line in spamreader:
        if linha2:
            return line[6][:7]
        linha2= True

def copiar_meio_final(spamreader, arquivoFinal, dataComeco)->None:
    """Copia os dados do arquivo a partir da dataComeco

    Args:
        spamreader (_type_): Dados do csv
        arquivoFinal (_type_): Arquivo onde será escrito os dados
        dataFinal (_type_): Data final, condição de inicialização de cópia.
    """

    achouPeriodoInicial = False
    for row in spamreader:
        if achouPeriodoInicial:
            for item in row:
                arquivoFinal.write(item+';')
            arquivoFinal.write('\n')
        elif dataComeco in row[-2]:
            achouPeriodoInicial = True

def copiar_comeco_meio(spamreader, arquivoFinal, dataFinal)->None:
    """Copia os dados do arquivo até encontrar a dataFinal

    Args:
        spamreader (_type_): Dados do csv
        arquivoFinal (_type_): Arquivo onde será escrito os dados
        dataFinal (_type_): Data final, condição de parada.
    """
    for row in spamreader:
        if dataFinal not in row[-2]:
            for item in row:
                arquivoFinal.write(item+';')
            arquivoFinal.write('\n')
        else:
            break

def renomear_todos_arquivos(path: str):
    """Renomeia todos os arquivos para o nome da cidade da medicao (conforme o item municipio) e o mês do arquivo

    Args:
        path (str): Path para a pasta com os arquivos
    """
    arquivosCsv = [file for file in os.listdir(path) if '.csv' in file]

    for file in arquivosCsv:
        with open(f'{path}/{file}', 'r', encoding="utf8") as f:
            spamreader = csv.reader(f, delimiter=';')
            mes = pega_mes_ano(spamreader)
            nomeEstacao = pega_nome(spamreader)
        os.rename(f'{path}/{file}', f'{path}/{nomeEstacao}-{mes}.csv')

def tratar_dados_cemaden(pathBrutos:str, dataComeco:str, dataFinal:str)->None:
    """Tratamento de dados dos arquivos do CEMADEN. Só funciona para pegar datas entre 04/2024 e 05/2024.

    Args:
        pathBrutos (str): path para o diretório com os arquivos de abril e maio
        dataComeco (str): data inicial de abril que será copiada
        dataFinal (str): data final que para a cópia dos dados (não inclusa)
    """
    #PROVAVEIS ERROS: 
    #SE TIVER MAIS DE UM ARQUIVOS COM O MESMO {Nome Estacap (municipio)} + {mes/ano}
    #SE A DATA FINAL NAO EXISTIR NO ARQUIVO DE MAIO
    #----
    #em algum momento deixei de seguir a padronização de váriaveis.
    renomear_todos_arquivos(pathBrutos)

    todosArquivos = os.listdir(pathBrutos)

    arquivosAbril = [file for file in todosArquivos if '04' in file]
    arquivosMaio = [file for file in todosArquivos if '05' in file]
    arquivosFinal = list()

    for fileAbril in arquivosAbril:
        with open(f'{pathBrutos}/{fileAbril}', 'r', encoding="utf8") as f:
            spamreader = csv.reader(f, delimiter=';')
            arquivosFinal.append(f'Dados-Processados/CEMADEN/{pega_nome(spamreader)}.csv')
            
            with open(arquivosFinal[-1], 'w', encoding="utf8") as fFinal:
                f.seek(0)
                copiar_header_CEMADEN(spamreader, fFinal)
                copiar_meio_final(spamreader, fFinal, dataComeco)

    for fileMaio, pathFinal in zip(arquivosMaio, arquivosFinal):
        with open(f'{pathBrutos}/{fileMaio}', 'r', encoding='utf8') as f:
            spamreader = csv.reader(f, delimiter=';')
            next(f)

            with open(pathFinal, 'a', encoding="utf8") as fFinal:
                copiar_comeco_meio(spamreader, fFinal, dataFinal)