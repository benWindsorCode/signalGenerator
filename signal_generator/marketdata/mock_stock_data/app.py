from flask import Flask
import requests
import random


app = Flask(__name__)
high = 300
close = 500
latestPrice = 240

def _get_fake_data():
    data = {
            'high':high,
            'close':close,
            'latestPrice':latestPrice+random.randint(1,10)
    } 
    return data

@app.route('/stock/<ticker>')
def show_stock(ticker: str):
    print("Fetching data for {}".format(ticker))
    return _get_fake_data() 

@app.route('/stock/<ticker>/<property>')
def show_stock_property(ticker: str, property: str):
    data = _get_fake_data()
    return str(data[property])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
