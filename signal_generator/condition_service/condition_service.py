from flask import Flask
from flask import request
from flask_cors import cross_origin
import yaml
import mysql.connector
import requests

app = Flask(__name__)

def getDb():
    with open("../config/database_connection_details.yaml", 'r') as yaml_file:
        cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    return mysql.connector.connect(
        host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['passwd'],
        database=cfg['mysql']['database']
    )

@app.route('/condition/add', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost')
def condition_add():
    mydb = getDb()
    mycursor = mydb.cursor()
    data = request.get_json()

    sql = "INSERT INTO sig_gen.condition (user_id, condition_text, notification_method, symbol) VALUES (%s, %s, %s, %s)"
    vals = (data['user_id'], data['condition_text'], data['notification_method'], data['symbol'])
    print(data)

    mycursor.execute(sql, vals)
    mydb.commit()
    mydb.disconnect()
    return 'COMPETE'

@app.route('/condition/<idcondition>', methods=['GET'])
def condition_get(idcondition):
    mydb = getDb()
    mycursor = mydb.cursor()
    mycurson.execute('SELECT * FROM sig_gen.condition WHERE idcondition = {}'.format(idcondition))
    result = mycursor.fetchone()
    mydb.disconnect()
    return result

