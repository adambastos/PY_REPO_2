from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcula_age(data_nasc):
    hoje = datetime.today().date() # Obtém a data atual (apenas data, sem hora)
    idade = relativedelta(hoje, data_nasc)  # Calcula a diferença
    return f"{idade.years} anos, {idade.months} meses e {idade.days} dias."

data_passada = datetime(1998, 10, 3).date()
resultado = calcula_age(data_passada) 

print(f'Sua idade hoje: {resultado}')