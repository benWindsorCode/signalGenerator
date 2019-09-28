from flask import Flask
import requests

app = Flask(__name__)
f = open('IEX_connection_details.txt', 'r')
API_token = f.read()[:-1]
f.close()

def _get_stock_data_json(ticker):
    query_string = 'https://cloud.iexapis.com/stable/stock/{}/quote?token={}'.format(ticker.lower(), API_token)
    result = requests.get(url = query_string) 
    return result.json()

@app.route('/stock/<ticker>')
def show_stock(ticker: str):
    print("Fetching data for {}".format(ticker))
    return _get_stock_data_json(ticker) 

@app.route('/stock/<ticker>/<property>')
def show_stock_property(ticker: str, property: str):
    data = _get_stock_data_json(ticker)
    return str(data[property])
