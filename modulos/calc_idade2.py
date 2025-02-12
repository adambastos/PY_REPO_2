from dateutil.relativedelta import relativedelta
from datetime import datetime, date

def calcula_idade(ano, mes, dia):
    nasc = date(ano, mes, dia)
    hoje = datetime.today().date()
    idade = relativedelta(hoje, nasc)
    return f"{idade.years} anos, {idade.months} meses e {idade.days} dias"

ano = int(input('Ano: '))
mes = int(input('mes: '))
dia = int(input('Dia: '))
resultado = calcula_idade(ano, mes, dia)
print(f'Sua idade hoje: {resultado}')


