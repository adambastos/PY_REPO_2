from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

def verifica_hora(data_hora):
    if 9 <= data_hora.hour < 17:
        return "Aberto!"
    else:
       return "Fechado"

# Criando datetime com fuso UTC para referência
get_fusos = datetime.now(ZoneInfo("UTC"))  # Corrigido: define UTC como referência
print(get_fusos)

# Convertendo para diferentes fusos horários
fh_sp = get_fusos.astimezone(ZoneInfo("America/Sao_Paulo"))
fh_tk = get_fusos.astimezone(ZoneInfo("Asia/Tokyo"))
fh_ny = get_fusos.astimezone(ZoneInfo("America/New_York"))

print("São Paulo:", fh_sp, verifica_hora(fh_sp))
print("Tóquio:", fh_tk, verifica_hora(fh_tk))
print("Nova York:", fh_ny, verifica_hora(fh_ny))



