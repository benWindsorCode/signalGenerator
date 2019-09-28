import boto3
from flask import Flask
from flask import request
import requests

app = Flask(__name__)
sns = boto3.client('sns')
f = open("test_topic_details.txt", 'r')
test_topic = f.read()[:-1]
f.close()

@app.route('/notify/text', methods=['GET', 'POST'])
def notify_user_text():
    message = request.args.get('message')
    # Publish a simple message to the specified SNS topic
    response = sns.publish(
            TopicArn=test_topic,
            Message=message,    
            MessageAttributes={
                'destination': {
                        'DataType':'String',
                        'StringValue':'sms'
                    }
                }
    )
    number = request.args.get('number')
    return "Sending msg: {}, to number: {}".format(message, number)

@app.route('/notify/email', methods=['GET', 'POST'])
def notify_user_email():

    message = request.args.get('message')
    # Publish a simple message to the specified SNS topic
    response = sns.publish(
            TopicArn=test_topic,
            Message=message,    
            Subject='Signal trigger notification',
            MessageAttributes={
                'destination': {
                        'DataType':'String',
                        'StringValue':'email'
                    }
                }
    )
    email = request.args.get('email')
    return "Sending msg: {}, to email: {}".format(message, email)
    
