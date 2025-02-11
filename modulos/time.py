import time

data_hoje = time.ctime() #Pegando a data de hoje
print(data_hoje)

print('Começando')
#time.sleep(5) #Espera 5 segundos para rodar o comando abaixo
print('O programa esperou 5 segundos para rodar')

hora_geral = time.gmtime() #Possibilita obter os dados do horário geral UTC
hora_local = time.localtime() #Dados do horário local

dia = hora_local.tm_mday
mes = hora_local.tm_mon
ano = hora_local.tm_year

print(f'A data atual: {dia}/{mes}/{ano}')
