import time
import pandas as pd
from iqoptionapi.stable_api import IQ_Option
import talib  # Certifique-se de que o talib está importado

email = "fag.almeida2@gmail.com"
password = "*Flavia01071999"

iq_option = IQ_Option(email, password)
iq_option.connect()

def check_connection():
    attempts = 0
    while not iq_option.check_connect() and attempts < 5:
        print("Erro ao conectar, tentando novamente...")
        iq_option.connect()
        time.sleep(15)
        attempts += 1
    return iq_option.check_connect()

def get_candles():
    attempts = 0
    while attempts < 5:
        candles = iq_option.get_candles("EURUSD", 60, 200, time.time())  # Buscar 200 velas
        if candles:
            # Convertendo o timestamp para data e hora legível
            for candle in candles:
                candle['datetime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(candle['from']))
            return candles
        else:
            print("Erro ao obter candles, tentando novamente em 15 segundos...")
            time.sleep(15)
            attempts += 1
    return None

def salvar_dados_csv(dados, caminho_arquivo='dados_mercado.csv'):
    df = pd.DataFrame(dados)
    df.to_csv(caminho_arquivo, index=False)

def analisar_dados():
    try:
        dados_mercado = pd.read_csv('dados_mercado.csv')
        dados_mercado['datetime'] = pd.to_datetime(dados_mercado['datetime'])
        
        # Calculando a SMA (Simple Moving Average)
        dados_mercado['SMA'] = talib.SMA(dados_mercado['close'], timeperiod=10)

        # Calculando o RSI (Relative Strength Index)
        dados_mercado['RSI'] = talib.RSI(dados_mercado['close'], timeperiod=14)

        print(dados_mercado)
        return dados_mercado
    except FileNotFoundError:
        print("Arquivo 'dados_mercado.csv' não encontrado.")
        return None

def main():
    if check_connection():
        print("Conectado com sucesso!")
        dados = get_candles()
        if dados:
            print("Dados coletados com sucesso!")
            salvar_dados_csv(dados)
        else:
            print("Não foi possível coletar dados.")

    # Analisar dados de mercado
    analisar_dados()

if __name__ == "__main__":
    main()
