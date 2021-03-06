from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import cross_origin
import yaml
import mysql.connector
import requests

app = Flask(__name__)

def getDb():
    with open("database_connection_details.yaml", 'r') as yaml_file:
        cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    return mysql.connector.connect(
        host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['passwd'],
        database=cfg['mysql']['database']
    )

def get_conditions_from_results(results):
    conditions = []
    for result in results:
        dict_result = { 
                'idcondition':result[0], 
                'user_id':result[1], 
                'condition_text':result[2], 
                'notification_method':result[3], 
                'symbol':result[4], 
                'last_value':result[5], 
                'is_active':result[6],
                'condition_name':result[7]
        }
        conditions.append(dict_result)

    return conditions

@app.route('/condition/add', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def condition_add():
    mydb = getDb()
    mycursor = mydb.cursor(prepared=True)
    data = request.get_json()

    sql = "INSERT INTO sig_gen.condition (user_id, condition_text, notification_method, symbol) VALUES (%s, %s, %s, %s)"
    vals = (data['user_id'], data['condition_text'], data['notification_method'], data['symbol'])
    print(data)

    mycursor.execute(sql, vals)
    mydb.commit()
    mydb.disconnect()
    return 'COMPETE'

@app.route('/condition/<idcondition>', methods=['GET'])
@cross_origin(origin='*')
def condition_get(idcondition):
    mydb = getDb()
    mycursor = mydb.cursor(prepared=True)
    mycursor.execute('SELECT * FROM sig_gen.condition WHERE idcondition = {}'.format(idcondition))
    result = mycursor.fetchone()
    mydb.disconnect()
    return jsonify(get_conditions_from_results([result])[0])

@app.route('/condition/user/<user_id>', methods=['GET'])
@cross_origin(origin='*')
def condition_by_user_get(user_id):
    mydb = getDb()
    mycursor = mydb.cursor(prepared=True)
    mycursor.execute('SELECT * FROM sig_gen.condition WHERE user_id = {}'.format(user_id))
    result = mycursor.fetchall()
    mydb.disconnect()
    return jsonify(get_conditions_from_results(result))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001, debug=True)
