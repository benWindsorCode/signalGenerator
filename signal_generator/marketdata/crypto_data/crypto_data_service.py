from flask import Flask
import requests
import yaml


app = Flask(__name__)
with open('../../config/service_connection_details.yaml', 'r') as yaml_file:
    cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

API_token = cfg['cryptocompare']['API_key']

def _get_crypto_data_json(crypto_asset, fiat_currency):
    query_string = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}&api_key={}'.format(crypto_asset, fiat_currency, API_token)
    # query_string = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&api_key={}'.format(crypto_asset, fiat_currency, API_token)
    result = requests.get(url = query_string) 
    return result.json()['RAW'][crypto_asset][fiat_currency]

@app.route('/crypto/<symbol>')
def show_stock(symbol: str):
    print("Fetching data for {}".format(symbol))
    # todo: implement check to ensure symbol is correct format
    split = symbol.split('-')
    return _get_crypto_data_json(split[0], split[1]) 
