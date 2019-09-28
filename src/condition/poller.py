import time
import requests
import pickle
from condition import Condition

test_data = [
        { 'username':'ben', 'notification_type':'SMS', 'condition':'latestPrice < 245', 'symbol':'AAPL', 'last_value':False },
        { 'username':'james', 'notification_type':'EMAIL', 'condition':'latestPrice < 100', 'symbol':'MSFT', 'last_value':False }
        ]

def detect_change(data):
    for i in range(len(data)):
        item = data[i]
        condition = Condition(item['condition'])
        query_string = 'http://127.0.0.1:5010/marketdata/{}'.format(item['symbol'])
        dat = requests.get(url = query_string).json()
        print(dat)
        print(condition.evaluate(dat))
        if condition.evaluate(dat) and item['last_value'] != True:
            print(item)
            print("last_value: {}".format(item['last_value']))
            item['last_value'] = True
            print(item)
            data[i] = item
            if item['notification_type'] == 'SMS':
                print('notifying')
                query_string = 'http://127.0.0.1:5003/notify/text?message={}:%20{}&number=test_num'.format(item['symbol'], item['condition'])
                requests.post(url = query_string)
            elif item['notification_type'] == 'EMAIL':
                query_string = 'http://127.0.0.1:5003/notify/email?message={}:%20{}&email=test_address'.format(item['symbol'], item['condition'])
                requests.post(url = query_string)
            elif item['notification_type'] == 'BOTH':
                pass
        elif condition.evaluate(dat) == False:
            item['last_value'] = False
            data[i] = item
    return data

while True:
    print(test_data)
    test_data = detect_change(test_data)

    time.sleep(3)
