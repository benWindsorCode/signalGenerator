# Signal Generator
A custom signal generation program.
# To Run
Place your IEX publishable API key in a file called IEX\_connection\_details.txt in the src/marketdata folder.

Run the following commands from inside the marketdata folder:

export FLASK\_ENV=development
export FLASK\_APP=market\_data\_service.py

flask run --port 5000

Navigate to the notification service folder and run:

export FLASK\_APP=notification\_service.py

flask run --port 5001
