from flask import Flask
from flask import request
import yaml
import mysql.connector
import requests

app = Flask(__name__)

@app.route('/user/add', methods=['POST'])
def user_add():
    with open('database_connection_details.yaml', 'r') as yaml_file:
        cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    mydb = mysql.connector.connect(
        host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['passwd'],
        database=cfg['mysql']['database']
    )

    mycursor = mydb.cursor()
    data = request.get_json()

    sql = "INSERT INTO sig_gen.user (username, sms_number, email) VALUES (%s, %s, %s)"
    vals = (data['username'], data['sms_number'], data['email'])

    mycursor.execute(sql, vals)
    mydb.commit()
    mydb.disconnect()
    return 'COMPETE'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
