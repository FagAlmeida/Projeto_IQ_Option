from iqoptionapi.stable_api import IQ_Option

def testar_conexao():
    email = "fag.almeida2@gmail.com"
    senha = "*Flavia01071999"

    iq = IQ_Option(email, senha)
    status, msg = iq.connect()
    if status:
        print("Conectado com sucesso!")
        # Testar chamada simples
        try:
            velas = iq.get_candles("EUR/USD", 60, 1, time.time())
            if velas:
                print("Dados coletados com sucesso!")
                print(velas)
            else:
                print("Nenhum dado retornado.")
        except Exception as e:
            print(f"Erro ao obter dados: {e}")
    else:
        print(f"Falha na conexão: {msg}")

testar_conexao()
