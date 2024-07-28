from flask import Flask, jsonify, send_from_directory, request
import pandas as pd
import os
from coletar_dados_iqoption import conectar, coletar_dados

app = Flask(__name__, static_folder='')

@app.route('/')
def serve_index():
    return send_from_directory(os.path.join(os.getcwd(), 'projeto-signals'), 'index.html')

@app.route('/dados_mercado', methods=['GET'])
def get_dados_mercado():
    dados = pd.read_csv('dados_mercado.csv')
    return jsonify(dados.to_dict(orient='records'))

@app.route('/start_bot', methods=['GET'])
def start_bot():
    currency = request.args.get('currency')
    iq = conectar()
    if iq.check_connect():
        sinais = coletar_dados(iq, currency)
        return jsonify({'signals': sinais})
    else:
        return jsonify({'error': 'Erro ao conectar com a IQ Option'}), 500

if __name__ == '__main__':
    app.run(debug=True)
