# Signal Generator
A custom signal generation program, designed to take conditions from users such as 'AAPL price > $500 or AAPL price < $300' and send a text or email (or both) to the user to alert them when this condition triggers. This allows users to create their own signals out of combinations of boolean statements which the framework will periodically evaluate using a market data service to allow access to various assets.
# Code Structure
The code is split into two main directories:
- signal_generator = the python backend
- signal-generator-site = the Angular backed frontend which is very rough/WIP

The backend uses a containerised microservice architecture, with services as follows:
- Market data service. In signal_generator/marketdata we have a proxy which points to various sources of market data. This proxy can also be pointed to mock market data sources
- Condition service. In signal_generator/condition_service this service allows for addition of conditions to the backend storage
- Notification service. In signal_generator/notification_service this service allows for the sending of notifications to users. Notifications are sent via AWS.
- Subscription service. In signal_generator/subscription_service this service deals with adding new AWS subscriptions for users, setting up the phone number/email for a user (this is WIP)
- User service. In signal_generator/user_service, this service adds users to the backend, it needs input sanitising and carefully cleaning before production use (this is WIP)

Each service is designed to be span up in a containerised environment, locally I used docker compose. This is to allow for easy scaling of market data services for example, giving the option to flexibly expand per data source the amount of resources required.
# Dependancies 
If using a venv create your venv, run 'source venv/bin/activate', install the packages in requirements.txt, run 'deactivate' when ready to leave the venv.
# To Run
Place your mysql database connection details in a file called database\_connection\_details.yaml in the config folder
Place your test AWS SNS API key in a file caled test\_topic\_details.txt in the src/notification folder.
Place your IEX and Cryptocompare API keys in a file called service\_connection\_details.yaml in the config folder

Run the following commands from inside the stock\_data folder (note the mock endpoint you can also run here):
export FLASK\_ENV=development
export FLASK\_APP=stock\_data\_service.py
flask run --port 5000

Run the following commands from inside the crypto\_data folder:
export FLASK\_ENV=development
export FLASK\_APP=crypto\_data\_service.py
flask run --port 5001

Run the following commands from inside the fx\_data folder:
export FLASK\_ENV=development
export FLASK\_APP=fx\_data\_service.py
flask run --port 5002

Run the following commands from inside the marketdata folder:
export FLASK\_ENV=development
export FLASK\_APP=market\_data\_proxy.py
flask run --port 5010

Run the following commands from the notification service folder and run:
export FLASK\_ENV=development
export FLASK\_APP=notification\_service.py
flask run --port 6001

Run the following commands from the user service folder and run:
export FLASK\_ENV=development
export FLASK\_APP=user\_service.py
flask run --port 6000

