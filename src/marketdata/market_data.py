from flask import Flask
import requests

app = Flask(__name__)
f = open('IEX_connection_details.txt', 'r')
API_token = f.read()[:-1]
f.close()

@app.route('/')
def index():
    return 'Server Works!'
  
@app.route('/stock/<ticker>')
def show_stock_price(ticker: str):
    query_string = 'https://cloud.iexapis.com/stable/stock/{}/quote?token={}'.format(ticker.lower(), API_token)
    print(query_string)
    result = requests.get(url = query_string) 
    print("Fetching data for {}".format(ticker))
    return result.json() 
