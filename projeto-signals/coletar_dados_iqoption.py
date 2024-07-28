import time
import pandas as pd
from iqoptionapi.stable_api import IQ_Option

def conectar():
    iq = IQ_Option("fag.almeida2@gmail.com", "*Flavia01071999")
    iq.connect()
    return iq

def coletar_dados(iq, paridade):
    intervalo = 60  # Em segundos
    while True:
        try:
            velas = iq.get_candles(paridade, intervalo, 10, time.time())
            dados = pd.DataFrame(velas)
            dados['SMA'] = dados['close'].rolling(window=10).mean()
            dados['RSI'] = 100 - (100 / (1 + dados['close'].diff().rolling(window=14).apply(lambda x: (x[x > 0].sum() / abs(x[x < 0]).sum()) if abs(x[x < 0]).sum() != 0 else 0)))
            sinais = sinais_trading(dados)
            return sinais
        except Exception as e:
            print(f"Erro ao coletar dados: {e}. Tentando reconectar...")
            iq.connect()
            time.sleep(5)

def sinais_trading(dados):
    sinais = []
    for i in range(len(dados)):
        horario = time.strftime('%H:%M:%S', time.localtime(dados['from'][i]))
        if dados['RSI'][i] < 30 and dados['close'][i] < dados['SMA'][i]:
            sinais.append({'tipo': 'Compra', 'horario': horario})
        elif dados['RSI'][i] > 70 and dados['close'][i] > dados['SMA'][i]:
            sinais.append({'tipo': 'Venda', 'horario': horario})
        else:
            sinais.append({'tipo': 'Neutro', 'horario': horario})
    return sinais

if __name__ == "__main__":
    iq = conectar()
    if iq.check_connect():
        coletar_dados(iq, "EURUSD")
    else:
        print("Erro ao conectar com a IQ Option")
