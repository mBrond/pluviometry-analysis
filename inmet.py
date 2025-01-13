import csv
from datetime import datetime, timedelta 
import os

import utilidades

def checar_data_em_linha(row, dateAtual)->bool:
    diaAtual = dateAtual.strftime("%Y/%m/%d")
    return diaAtual in row

def copiar_header_INMET(arquivoSource: str, arquivoFinal: str)->None:
    with open(arquivoSource, 'r') as f, open(arquivoFinal, "w") as fFinal:
        spamreader = csv.reader(f, delimiter=';')
        for index, row in enumerate(spamreader):
            if index>8: #primeiras 9 linhas são o cabeçalho
                break
            for item in row:
                fFinal.write(item+';')
            fFinal.write('\n')

def escreve_linha(row, fFinal):
    for item in row:
        fFinal.write(item+';')
    fFinal.write('\n')

def separar_arquivos_inmet(dirSource, dirEnd): #funcionando
    """Move arquivos das correspondentes estações do INMET descritas em 'estacoes.csv' presentes em 'dirSource' para 'dirEnd'

    Args:
        dirSource (str): Diretório inicial dos arquivos
        dirEnd (str): Diretório final dos arquivos
    """
    path_estacoes = 'estacoes.csv'
    tipo_estacoes = 'INMET'
    codigos = utilidades.pegar_estacoes(path_estacoes, tipo_estacoes)

    todosArquivosInmet = utilidades.get_all_files(dirSource)

    arquivosSeparados = [arq for arq in todosArquivosInmet if any(codigo in arq for codigo in codigos)]

    for arq in arquivosSeparados:
        os.rename(dirSource+arq, dirEnd+arq)


def separar_periodo_inmet(dateInicial: datetime, dateFinal: datetime, arquivoSource: str, arquivoFinal: str):
    """_summary_

    Args:
        dateInicial (datetime): _description_
        dateFinal (datetime): _description_
        arquivoSource (str): _description_
        arquivoFinal (str): _description_
    """
    copiar_header_INMET(arquivoSource, arquivoFinal)

    dateAtual = dateInicial
    dateFinal += timedelta(days=1)

    with open(arquivoSource, 'r') as f, open(arquivoFinal, 'a') as fFinal:
        spamreader = csv.reader(f, delimiter=';')

        achouPrimeiraData = False

        for row in spamreader:
            if checar_data_em_linha(row, dateAtual):
                escreve_linha(row, fFinal)
                achouPrimeiraData = True
            elif achouPrimeiraData:
                dateAtual += timedelta(days=1)

            if dateAtual == dateFinal:
                break


# arquivoSource =  'Dados-Processados/INMET/INMET_S_RS_A801_PORTO ALEGRE - JARDIM BOTANICO_01-01-2024_A_30-11-2024.CSV'
# arquivoFinal = 'Dados-Processados/teste/t.csv'
# dataComeco = datetime(2024, 4, 17)
# dataFinal = datetime(2024, 5, 25)
# # copiar_header_INMET(arquivoSource, arquivoFinal)

# separar_periodo_inmet(dataComeco, dataFinal, arquivoSource, arquivoFinal)