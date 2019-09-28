import time
import requests
import pickle
from condition import Condition

test_data = [
        { 'username':'ben', 'notification_type':'SMS', 'condition':'latestPrice < 450', 'symbol':'AAPL' },
        { 'username':'james', 'notification_type':'EMAIL', 'condition':'latestPrice < 430', 'symbol':'MSFT' }
        ]

while True:
    for item in test_data:
        condition = Condition(item['condition'])
        query_string = 'http://127.0.0.1:5010/marketdata/{}'.format(item['symbol'])
        dat = requests.get(url = query_string).json()
        print(dat)
        print(condition.evaluate(dat))
        if condition.evaluate(dat):
            if item['notification_type'] == 'SMS':
                query_string = 'http://127.0.0.1:5003/notify/text?message={}:%20{}&number=test_num'.format(item['symbol'], item['condition'])
                requests.post(url = query_string)
            elif item['notification_type'] == 'EMAIL':
                query_string = 'http://127.0.0.1:5003/notify/email?message={}:%20{}&email=test_address'.format(item['symbol'], item['condition'])
                requests.post(url = query_string)
            elif item['notification_type'] == 'BOTH':
                pass


    time.sleep(5000)
