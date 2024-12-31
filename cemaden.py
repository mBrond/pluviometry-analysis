import csv

def copiar_header_CEMADEN(spamreader, arquivoFinal)->None:
    for row in spamreader:
        for item in row:
            arquivoFinal.write(item+';')
        break
    arquivoFinal.write('\n')

def pega_nome(spamreader)->str:
    linha2 = False
    for line in spamreader:
        if linha2:
            return line[0]
        linha2= True

def copiar_meio_final(spamreader, arquivoFinal, dataComeco)->None:
    achouPeriodoInicial = False
    for row in spamreader:
        if achouPeriodoInicial:
            for item in row:
                arquivoFinal.write(item+';')
            arquivoFinal.write('\n')
        elif dataComeco in row[-2]:
            achouPeriodoInicial = True

def copiar_comeco_meio(spamreader, arquivoFinal, dataFinal)->None:
    for row in spamreader:
        if dataFinal not in row[-2]:
            for item in row:
                arquivoFinal.write(item+';')
            arquivoFinal.write('\n')

def renomear_todos_arquivos(path: str):
    """Renomeia todos os arquivos para o nome da cidade da medicao (conforme o item municipio)

    Args:
        path (str): Path para a pasta com os arquivos
    """
    pass

def main():
    fileAbril = 'Dados-Brutos/CEMADEN/abril/data.csv'
    fileMaio = ''

    dataComeco = '2024-04-27'
    dataFinal = '2024-04-15'

    with open(fileAbril, 'r', encoding="utf8") as f:
        spamreader = csv.reader(f, delimiter=';')
        pathFinal = f'Dados-Processados/CEMADEN/{pega_nome(spamreader)}.csv'
        
        with open(pathFinal, 'w', encoding="utf8") as fFinal:
            f.seek(0)
            copiar_header_CEMADEN(spamreader, fFinal)
            # copiar_meio_final(spamreader, fFinal, dataComeco)


    #TROCAR ARQUIVO QUE ESTA SENDO ABERTO
    with open(fileAbril, 'r', encoding='utf8') as f:
        spamreader = csv.reader(f, delimiter=';')
        next(f)

        with open(pathFinal, 'a', encoding="utf8") as fFinal:
            copiar_comeco_meio(spamreader, fFinal, dataFinal)



main()