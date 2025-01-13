import os
import pandas as pd
from datetime import datetime 

import utilidades
from cemaden import tratar_dados_cemaden
from inmet import separar_arquivos_inmet, separar_periodo_inmet


def main():
    pathBrutos = 'Dados-Brutos'
    pathProcessados = 'Dados-Processados'

    utilidades.criar_pastas(pathBrutos, pathProcessados)
    
    #CEMADEN
    #Cada download no CEMADEN consiste em um arquivo com dados de uma estação no período de um mês
    #Tem captcha, download manual
    tratar_dados_cemaden(pathBrutos+'\\CEMADEN', '2024-04-27', '2024-05-15')

    utilidades.converter_csv_para_xls(pathProcessados+'\\CEMADEN')
    # utilidades.apagar_nao_csv(pathProcessados+'\\CEMADEN')

    #INMET
    #Cada download do INMET consiste no download um ZIP com vários arquivos separados por estação, no período de um ano 
    separar_arquivos_inmet(f'{pathBrutos}\\INMET\\', f'{pathProcessados}\\INMET\\')

    dataComeco = datetime(2024, 4, 17)
    dataFinal = datetime(2024, 5, 25)
    for nomeArquivo in utilidades.get_all_files(f'{pathProcessados}\\INMET\\'):
        arquivoFinal = f'{pathProcessados}\\INMET\\csv\\{nomeArquivo}'
        separar_periodo_inmet(dataComeco, dataFinal, f'{pathProcessados}\\INMET\\{nomeArquivo}', arquivoFinal)
    utilidades.converter_csv_para_xls_externo(f'{pathProcessados}\\INMET\\csv', f'{pathProcessados}\\INMET\\xls')

if __name__ == '__main__':
    main()