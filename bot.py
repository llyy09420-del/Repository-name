import ccxt
import time
from flask import Flask
import threading

# --- Flask Server to keep the bot alive on Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Status: Active"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# --- OKX API Configuration ---
params = {
    'apiKey': '9a3d6d8a-065c-4d1a-9073-db0ed6473ebd',
    'secret': 'A6B6C16AC035262F8B840052D9916B7B',
    'password': 'asdFF124$', 
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
}

exchange = ccxt.okx(params)
symbol = 'PEPE/USDT:USDT'
amount = 120000 

def start_bot():
    print("🚀 Starting PEPE Sniper...")
    while True:
        try:
            # Fetch current ticker
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            print(f"Current PEPE Price: {price}")
            
            # Monitoring loop - updates every 10 seconds
            time.sleep(10)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    # Run Web Server in Background
    threading.Thread(target=run_web).start()
    # Start Trading Bot
    start_bot()
