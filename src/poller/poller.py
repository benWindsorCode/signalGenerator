import time
import requests

while True:
    query = "http://127.0.0.1:5000/stock/msft/latestPrice"
    data = requests.get(url = query)
    print(data)
    print(data.json())
    time.sleep(5000)
