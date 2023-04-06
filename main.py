import requests
from datetime import datetime


def SendTelegramAlert(chat_id, message):
    # inicializa telegram
    TOKEN = 'coloque seu token aqui'
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    res = requests.get(api_url)


hoje = datetime.today()
data_lista = datetime(2023, 3, 11)
data_caca = datetime(2023, 3, 24)
grupo_CO = -861999374

SendTelegramAlert(grupo_CO, f"""
    Bom dia\n
    Faltam {(data_lista - hoje).days} dias para soltar a Lista
    Faltam {(data_caca - hoje).days} dias para o caça"""
)
