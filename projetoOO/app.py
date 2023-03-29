from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carregar o conjunto de dados
dataset = pd.read_csv('clientes.csv')

# Selecionar apenas as colunas de quartos e taxa de criminalidade
X = dataset[['conta_recente', 'cliente_recente', 'cnae_recente', 'faturamento_recente']].values

# Selecionar o preço como variável de saída
y = dataset['fraude'].values

# Treinar o modelo de regressão linear
regressor = LinearRegression()
regressor.fit(X, y)

# Criar o aplicativo Flask
app = Flask(__name__)

# Criar a rota para a API
@app.route('/predict', methods=['POST'])
def predict():
    # Obter os dados da solicitação POST
    data = request.get_json()

    # Converter os dados em um array numpy
    data = np.array([[data['conta_recente'], data['cliente_recente'], data['cnae_recente'], data['faturamento_recente']]])

    # Fazer a previsão com base nos dados de entrada
    prediction = regressor.predict(data)

    # Converter o resultado em um objeto JSON e retorná-lo
    result = {'Risco de Fraude:': prediction[0]}
    return jsonify(result)

# Executar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
