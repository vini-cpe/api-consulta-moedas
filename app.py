from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/cotacao/<moeda>')
def cotacao(moeda):
    url = f'https://api.exchangerate.host/latest?base={moeda.upper()}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
