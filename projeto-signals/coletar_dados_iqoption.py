import datetime
import pandas as pd
from iqoptionapi.stable_api import IQ_Option

def coletar_dados():
    # Configurar a API
    iq = IQ_Option('fag.almeida2@gmail.com', '*Flavia01071999')
    iq.connect()
    
    # Verificar a conexão
    if iq.check_connect():
        print("Conectado com sucesso!")
    else:
        print("Erro ao conectar.")
        return

    # Definir o ativo e o intervalo
    ativo = 'EURUSD'
    intervalo = '5m'  # Intervalo de 5 minutos
    data_fim = datetime.datetime.now()
    data_inicio = data_fim - datetime.timedelta(days=1)  # Últimos 1 dia

    # Coletar dados
    try:
        candles = iq.get_candles(ativo, intervalo, 1000, data_fim.timestamp())
        df = pd.DataFrame(candles)
        df['datetime'] = pd.to_datetime(df['datetime'], unit='s')
        df.to_csv('dados_mercado.csv', index=False)
        print("Dados coletados com sucesso!")
    except Exception as e:
        print(f"Erro ao coletar os dados: {e}")
    
    iq.logout()

if __name__ == "__main__":
    coletar_dados()
