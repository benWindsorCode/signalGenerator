from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/notify/text', methods=['GET', 'POST'])
def notify_user_text():
    message = request.args.get('message')
    number = request.args.get('number')
    print(message)
    return "Sending msg: {}, to number: {}".format(message, number)

@app.route('/notify/email', methods=['GET', 'POST'])
def notify_user_email():
    message = request.args.get('message')
    email = request.args.get('email')
    return "Sending msg: {}, to email: {}".format(message, email)
    
