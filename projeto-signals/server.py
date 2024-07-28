from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        dados = pd.read_csv('dados_mercado_com_sinais.csv')
        sinais = dados[['ativo', 'Sinal', 'datetime']].to_dict(orient='records')
        return render_template('index.html', sinais=sinais)
    except Exception as e:
        print(f"Erro ao carregar os sinais: {e}")
        return "Erro ao carregar os sinais."

@app.route('/sinais')
def sinais():
    try:
        dados = pd.read_csv('dados_mercado_com_sinais.csv')
        sinais = dados[['ativo', 'Sinal', 'datetime']].to_dict(orient='records')
        return jsonify(sinais)
    except Exception as e:
        print(f"Erro ao carregar os sinais: {e}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
