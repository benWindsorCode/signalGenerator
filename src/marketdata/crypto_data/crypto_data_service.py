from flask import Flask
import requests

app = Flask(__name__)
f = open('cryptocompare_connection_details.txt', 'r')
API_token = f.read()[:-1]
f.close()

def _get_crypto_data_json(crypto_asset, fiat_currency):
    query_string = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=GBP&api_key={}'.format(crypto_asset, fiat_currency, API_token)
    # query_string = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&api_key={}'.format(crypto_asset, fiat_currency, API_token)
    result = requests.get(url = query_string) 
    return result.json()['RAW'][crypto_asset][fiat_currency]

@app.route('/crypto/<symbol>')
def show_stock(symbol: str):
    print("Fetching data for {}".format(symbol))
    # todo: implement check to ensure symbol is correct format
    split = symbol.split('-')
    return _get_crypto_data_json(split[0], split[1]) 
