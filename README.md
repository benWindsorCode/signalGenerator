# Signal Generator
A custom signal generation program.
# To Run
Place your IEX publishable API key in a file called IEX\_connection\_details.txt in the src/marketdata/stock\_data folder.
Place your cryptocompare API key in a file called \cryptocompare\_connection\_details.txt in the src/marketdata/crypto\_data folder
Place your test AWS SNS API key in a file caled test\_topic\_details.txt in the src/notification folder.

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
