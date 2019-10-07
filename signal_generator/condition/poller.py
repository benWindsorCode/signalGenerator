import time
import requests
import pickle
import yaml
import mysql.connector
from condition import Condition
from notification_method import NOTIFICATION_METHOD
from condition_model import Condition_model
from user_model import User_model

marketdata_host = '127.0.0.1'
notification_service_host = '127.0.0.1'
notification_service_port = '5100'

def detect_change(data, mycursor):
    for i in range(len(data)):
        item = data[i]
        print(item.condition_text)
        print("last_value: {}".format(item.last_value))
        condition = Condition(item.condition_text)
        query_string = 'http://{}:5010/marketdata/{}'.format(marketdata_host, item.symbol)
        dat = requests.get(url = query_string).json()
        is_condition_true = condition.evaluate(dat)
        last_value = item.last_value
        item.last_value = is_condition_true
        data[i] = item
        print(dat)
        print(condition.evaluate(dat))

        # Only notify if true and it previously was not true, to avoid constant notifications
        if condition.evaluate(dat) and last_value != is_condition_true:
            user = fetch_user(item.user_id, mycursor)
            print('Notifying user: {}'.format(user.username))
            text = "{}%20your%20notification%20for%20{}:%20{}".format(user.username, item.symbol, item.condition_text)
            if item.notification_method == NOTIFICATION_METHOD.SMS:
                query_string = 'http://{}:{}/notify/text?message={}&number=test_num'.format(notification_service_host, notification_service_port, text)
                requests.post(url = query_string)
            elif item.notification_method == NOTIFICATION_METHOD.EMAIL:
                query_string = 'http://{}:{}/notify/email?message={}&email=test_address'.format(notification_service_host, notification_service_port, text)
                requests.post(url = query_string)
            elif item.notification_method == NOTIFICATION_METHOD.BOTH:
                query_string = 'http://{}:{}/notify/text?message={}&number=test_num'.format(notification_service_host, notification_service_port, text)
                requests.post(url = query_string)
                query_string = 'http://{}:{}/notify/email?message={}&email=test_address'.format(notification_service_host, notification_service_port, text)
                requests.post(url = query_string)
    return data

def convert_condition_to_object(results):
    condition_dicts = []
    for result in results:
        condition = Condition_model(result)
        condition_dicts.append(condition)
    return condition_dicts

def convert_user_to_object(result):
    return User_model(result)

def fetch_user(iduser, mycursor):
    mycursor.execute("SELECT * FROM sig_gen.user WHERE iduser = {}".format(iduser))
    result = mycursor.fetchone()
    return convert_user_to_object(result)

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
    

    # Find way to pull in new conditions without overriding the changed ones
    mycursor.execute("SELECT * FROM sig_gen.condition")
    results = mycursor.fetchall()
    condition_data = convert_condition_to_object(results)
    enabled_conditions = [ condition for condition in condition_data if condition.is_active == True ] 

    # todo: use a while True here instead
    while True:
        enabled_conditions = detect_change(enabled_conditions, mycursor)
        time.sleep(60)
        print("-------------------------------------------------------------\n\n")

    mydb.disconnect()

if __name__ == "__main__":
    run()
