from flask import Flask
from flask import request
import yaml
import mysql.connector
import requests

app = Flask(__name__)

@app.route('/condition/add', methods=['POST'])
def user_add():
    with open("../config/database_connection_details.yaml", 'r') as yaml_file:
        cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    mydb = mysql.connector.connect(
        host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['passwd'],
        database=cfg['mysql']['database']
    )

    mycursor = mydb.cursor()
    data = request.get_json()

    sql = "INSERT INTO sig_gen.condition (user_id, condition_text, notification_method, symbol) VALUES (%s, %s, %s, %s)"
    vals = (data['user_id'], data['condition_text'], data['notification_method'], data['symbol'])
    print(data)

    mycursor.execute(sql, vals)
    mydb.commit()
    mydb.disconnect()
    return 'COMPETE'
