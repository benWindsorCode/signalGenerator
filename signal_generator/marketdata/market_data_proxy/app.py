from flask import Flask
from flask_cors import cross_origin
import requests
import json

app = Flask(__name__)
hostname ="127.0.0.1"  # use 'host.docker.internal' if testing the containers locally

def _parse_stock(ticker):
    query_string = 'http://{}:5000/stock/{}'.format(hostname, ticker) 
    result = requests.get(url = query_string) 
    return result.json()

def _parse_currency(symbol):
    cryptos = { 'BTC', 'ETH', 'LTC', 'BCH', 'ETC' }
    base = symbol.split('-')[0]
    secondary = symbol.split('-')[1]
    if base in cryptos:
        query_string = 'http://{}:5001/crypto/{}-{}'.format(hostname, base, secondary) 
        result = requests.get(url = query_string) 
        return result.json()
    else:
        query_string = 'http://{}:5002/ccy/{}-{}'.format(hostname, base, secondary) 
        result = requests.get(url = query_string) 
        return result.json()

@app.route('/marketdata/<symbol>')
def fetch_data(symbol: str):
    print("Fetching data for {}".format(symbol))
    if symbol.find('-') != -1:
        return _parse_currency(symbol)
    else:
        return _parse_stock(symbol)

@app.route('/marketdata/<symbol>/properties')
@cross_origin(origin='*')
def show_properties(symbol: str):
    print("Fetching properties for {}".format(symbol))
    data = fetch_data(symbol)
    return json.dumps(list(data.keys()))

@app.route('/marketdata/health')
def return_health():
    return "I'm up"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
