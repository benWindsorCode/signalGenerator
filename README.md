# Signal Generator
A custom signal generation program.
# To Run
Place your mysql database connection details in a file called database\_connection\_details.yaml in the config folder
Place your test AWS SNS API key in a file caled test\_topic\_details.txt in the src/notification folder.
Place your IEX and Cryptocompare API keys in a file called service\_connection\_details.yaml in the config folder

Run the following commands from inside the stock\_data folder:

export FLASK\_ENV=development
export FLASK\_APP=stock\_data\_service.py
flask run --port 5000

Run the following commands from inside the crypto\_data folder:
export FLASK\_ENV=development
export FLASK\_APP=crypto\_data\_service.py
flask run --port 5001

Run the following commands from inside the marketdata folder:
export FLASK\_ENV=development
export FLASK\_APP=market\_data\_proxy.py
flask run --port 5002

Navigate to the notification service folder and run:
export FLASK\_ENV=development
export FLASK\_APP=notification\_service.py
flask run --port 5002
