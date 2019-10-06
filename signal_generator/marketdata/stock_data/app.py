from flask import Flask
import requests
import yaml

app = Flask(__name__)
with open('../../config/service_connection_details.yaml', 'r') as yaml_file:
    cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

API_token = cfg['IEX']['API_key']

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
