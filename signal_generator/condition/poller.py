import time
import requests
import pickle
import yaml
import mysql.connector
from condition import Condition
from notification_method import NOTIFICATION_METHOD


def detect_change(data, mycursor):
    for i in range(len(data)):
        item = data[i]
        print(item)
        condition = Condition(item['condition_text'])
        query_string = 'http://127.0.0.1:5010/marketdata/{}'.format(item['symbol'])
        dat = requests.get(url = query_string).json()
        print(dat)
        print(condition.evaluate(dat))
        if condition.evaluate(dat):
            user = fetch_user(item['user_id'], mycursor)
            text = "{}%20your%20notification%20for%20{}:%20{}".format(user['username'], item['symbol'], item['condition_text'])
            if item['notification_method'] == NOTIFICATION_METHOD.SMS:
                query_string = 'http://127.0.0.1:5003/notify/text?message={}&number=test_num'.format(text)
                requests.post(url = query_string)
            elif item['notification_method'] == NOTIFICATION_METHOD.EMAIL:
                query_string = 'http://127.0.0.1:5003/notify/email?message={}&email=test_address'.format(text)
                requests.post(url = query_string)
            elif item['notification_method'] == NOTIFICATION_METHOD.BOTH:
                query_string = 'http://127.0.0.1:5003/notify/text?message={}&number=test_num'.format(text)
                requests.post(url = query_string)
                query_string = 'http://127.0.0.1:5003/notify/email?message={}&email=test_address'.format(text)
                requests.post(url = query_string)
        elif condition.evaluate(dat) == False:
            item['last_value'] = False
            data[i] = item

def convert_condition_to_dict(results):
    condition_dicts = []
    for result in results:
        condition = {
                'idcondition':result[0],
                'user_id':result[1],
                'condition_text':result[2],
                'notification_method':NOTIFICATION_METHOD[result[3]],
                'symbol':result[4],
                'last_value':bool(result[5])
                }
        condition_dicts.append(condition)
    return condition_dicts

def convert_user_to_dict(result):
    user = {
            'iduser':result[0],
            'username':result[1],
            'sms_number':result[2],
            'email':result[3]
    }
    return user

def fetch_user(iduser, mycursor):
    mycursor.execute("SELECT * FROM sig_gen.user WHERE iduser = {}".format(iduser))
    result = mycursor.fetchone()
    return convert_user_to_dict(result)

def run():
    with open("../config/database_connection_details.yaml", 'r') as yaml_file:
        cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    mydb = mysql.connector.connect(
        host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['passwd'],
        database=cfg['mysql']['database']
    )
    mycursor = mydb.cursor()
    
    # todo: use a while True here instead
    for i in range(3):
        mycursor.execute("SELECT * FROM sig_gen.condition")
        results = mycursor.fetchall()
        condition_data = convert_condition_to_dict(results)
        detect_change(condition_data, mycursor)
        time.sleep(3)

    mydb.disconnect()

if __name__ == "__main__":
    run()
