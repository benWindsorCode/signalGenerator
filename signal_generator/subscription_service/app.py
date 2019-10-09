import boto3
from flask import Flask
from flask import request
import requests

app = Flask(__name__)
sns = boto3.client('sns', region_name='eu-west-1')

@app.route('/subscription/topic/add', methods=['POST'])
def create_topic():
    data = request.get_json()
    response = sns.create_topic(
            Name='{}_{}'.format(data['username'], data['iduser'])
    )

    reply = {}
    reply['HTTPStatusCode'] = response['ResponseMetadata']['HTTPStatusCode']
    if reply['HTTPStatusCode'] == 200:
        reply['TopicArn'] = response['TopicArn']

    return reply

@app.route('/subscription/add', methods=['POST'])
def add_subscription():
    return ""

@app.route('/notify/health')
def health():
    return 'Im Alive'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
    
