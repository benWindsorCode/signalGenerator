import boto3
from flask import Flask
from flask import request
import requests

app = Flask(__name__)
sns = boto3.client('sns', region_name='eu-west-1')

@app.route('/subscription/topic/create', methods=['POST'])
def create_topic():
    data = request.get_json()
    response = sns.create_topic(
            Name='{}_{}'.format(username, iduser)
    )
    print(response)
    return "Created"

@app.route('/subscription/add', methods=['POST'])
def add_subscription():

@app.route('/notify/health')
def health():
    return 'Im Alive'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
    
