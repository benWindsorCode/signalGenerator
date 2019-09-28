from flask import Flask
import requests

app = Flask(__name__)

def _parse_stock(ticker):
    query_string = 'http://127.0.0.1:5000/stock/{}'.format(ticker) 
    result = requests.get(url = query_string) 
    return result.json()

def _parse_currency(symbol):
    cryptos = ['BTC', 'ETH', 'LTC', 'BCH', 'ETC']
    base = symbol.split('-')[0]
    secondary = symbol.split('-')[1]
    if base in cryptos:
        query_string = 'http://127.0.0.1:5001/crypto/{}-{}'.format(base, secondary) 
        result = requests.get(url = query_string) 
        return result.json()
    else:
        raise Exception("{} not supported currency pair".format(symbol))

@app.route('/marketdata/<symbol>')
def show_stock(symbol: str):
    print("Fetching data for {}".format(symbol))
    if symbol.find('-') != -1:
        return _parse_currency(symbol)
    else:
        return _parse_stock(symbol)
