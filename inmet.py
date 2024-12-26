import csv
from datetime import datetime, timedelta 

def separar_periodo(dateInicial: datetime.datetime, dateFinal: datetime.datetime, arquivoSource: str, arquivoFinal: str):
    dateSeguinte = dateInicial + timedelta(days=1)
    diaAtual = dateInicial.strftime("%Y%M%D")

    with open(arquivoSource) as f, open(arquivoFinal) as fFinal:
        spamreader = csv.reader(f, delimiter=';')
        
        for row in spamreader:



arquivoSource =  'Dados-Processados/INMET/INMET_S_RS_A801_PORTO ALEGRE - JARDIM BOTANICO_01-01-2024_A_30-11-2024.CSV'
arquivoFinal = ''
dataComeco = datetime.datetime(2024, 4, 17)
dataFinal = datetime.datetime(2024, 5, 25)

separar_periodo('1', '1', arquivoSource, arquivoFinal)