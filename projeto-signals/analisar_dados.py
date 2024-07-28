import pandas as pd
import talib
import numpy as np

def carregar_dados(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        dados = dados.dropna(subset=['close'])
        return dados
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def calcular_indicadores(dados):
    try:
        dados['SMA'] = talib.SMA(dados['close'], timeperiod=10)
        dados['RSI'] = talib.RSI(dados['close'], timeperiod=14)
        return dados
    except Exception as e:
        print(f"Erro ao calcular indicadores: {e}")
        return None

def sinais_trading(dados):
    sinais = []
    for i in range(len(dados)):
        if pd.isna(dados['RSI'][i]) or pd.isna(dados['SMA'][i]):
            sinais.append('Neutro')
        elif dados['RSI'][i] < 30 and dados['close'][i] < dados['SMA'][i]:
            sinais.append('Compra')
        elif dados['RSI'][i] > 70 and dados['close'][i] > dados['SMA'][i]:
            sinais.append('Venda')
        else:
            sinais.append('Neutro')
    return sinais

def main():
    dados = carregar_dados('dados_mercado.csv')
    if dados is not None:
        dados = calcular_indicadores(dados)
        if dados is not None:
            dados['Sinal'] = sinais_trading(dados)
            dados.to_csv('dados_mercado_com_sinais.csv', index=False)
            print("Análise concluída e arquivo atualizado com sinais.")
        else:
            print("Erro ao calcular indicadores.")
    else:
        print("Erro ao carregar os dados.")

if __name__ == "__main__":
    main()
