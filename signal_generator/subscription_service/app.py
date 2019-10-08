import boto3
from flask import Flask
from flask import request
import requests

app = Flask(__name__)
sns = boto3.client('sns', region_name='eu-west-1')

@app.route('/subscription/topic/create', methods=['GET', 'POST'])
def create_topic():
    response = sns.create_topic(
            Name='test_topic'
    )
    return "Created"

@app.route('/notify/health')
def health():
    return 'Im Alive'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
    
