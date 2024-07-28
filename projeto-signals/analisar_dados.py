import pandas as pd

# Carregar os dados
dados = pd.read_csv('dados_mercado.csv')

# Calcular SMA e RSI
dados['SMA'] = dados['close'].rolling(window=10).mean()
dados['RSI'] = 100 - (100 / (1 + dados['close'].diff().rolling(window=14).apply(lambda x: (x[x > 0].sum() / abs(x[x < 0]).sum()) if abs(x[x < 0]).sum() != 0 else 0)))

# Função para determinar sinais de compra e venda
def sinais_trading(dados):
    sinais = []
    for i in range(len(dados)):
        if dados['RSI'][i] < 30 and dados['close'][i] < dados['SMA'][i]:
            sinais.append('Compra')
        elif dados['RSI'][i] > 70 and dados['close'][i] > dados['SMA'][i]:
            sinais.append('Venda')
        else:
            sinais.append('Neutro')
    return sinais

# Adicionar sinais de trading ao dataframe
dados['Sinal'] = sinais_trading(dados)

# Salvar o arquivo atualizado
dados.to_csv('dados_mercado_com_sinais.csv', index=False)
