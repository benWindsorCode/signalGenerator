from flask import Flask
import requests

app = Flask(__name__)

def _get_ccy_data_json(base, secondary):
    query_string = 'https://api.exchangeratesapi.io/latest?base={}'.format(base)
    result = requests.get(url = query_string) 
    data =  { secondary: result.json()['rates'][secondary] }
    return data

@app.route('/ccy/<symbol>')
def show_ccy(symbol: str):
    print("Fetching data for {}".format(symbol))
    # todo: implement check to ensure symbol is correct format
    split = symbol.split('-')
    return _get_ccy_data_json(split[0], split[1]) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
