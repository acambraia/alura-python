from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carregar o conjunto de dados
dataset = pd.read_csv('baseClientes.csv')

# Selecionar apenas as colunas com as informações relevantes
X = dataset[['contanova', 'dataconstituicao', 'datarelacionamento', 'atividadeeconomica', 'faturamento', 'quadrosocial', 'inadimplenciacontador', 'empresaprivada', 'faturamento5m']].values

# Selecionar a coluna com as informações de saida
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
    data = np.array([[data['contanova'], data['dataconstituicao'], data['datarelacionamento'], data['atividadeeconomica'], data['faturamento'], data['quadrosocial'], data['inadimplenciacontador'], data['empresaprivada'], data['faturamento5m']]])

    # Fazer a previsão com base nos dados de entrada
    prediction = regressor.predict(data)

    # Converter o resultado em um objeto JSON e retorná-lo
    result = {'Risco de Fraude:': prediction[0]}
    return jsonify(result)

# Executar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
