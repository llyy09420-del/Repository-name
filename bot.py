import ccxt
import time
from flask import Flask
from threading import Thread

# --- Flask Server for Render Continuity ---
app = Flask('')

@app.route('/')
def home():
    return "PEPE Trading Bot is Active!"

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
symbol = 'PEPE-USDT-SWAP'
# Amount set to approximately 1 USD (adjusting for PEPE units)
amount = 120000 

def start_bot():
    print("Bot starting... Monitoring PEPE-USDT")
    while True:
        try:
            # 1. Fetch current price
            ticker = exchange.fetch_ticker(symbol)
            price = float(ticker['last'])
            print(f"Current Price: {price:.8f}")

            # 2. Execute Market Buy
            print(f"Executing Buy Order for ~1 USD at {price:.8f}")
            # exchange.create_market_buy_order(symbol, amount)

            # 3. Setting Targets (1% Profit or 5% Loss)
            take_profit = price * 1.01
            stop_loss = price * 0.95

            print(f"Target: {take_profit:.8f} | Stop: {stop_loss:.8f}")

            # 4. Monitoring Loop
            while True:
                check_ticker = exchange.fetch_ticker(symbol)
                current_p = float(check_ticker['last'])
                
                if current_p >= take_profit:
                    print("Target Reached! Selling for profit.")
                    # exchange.create_market_sell_order(symbol, amount)
                    break
                elif current_p <= stop_loss:
                    print("Stop Loss hit. Selling to protect funds.")
                    # exchange.create_market_sell_order(symbol, amount)
                    break
                
                time.sleep(1) # Fast response

            print("Cycle completed. Waiting 30 seconds for next opportunity...")
            time.sleep(30)

        except Exception as e:
            print(f"Error encountered: {e}")
            time.sleep(30)

if __name__ == "__main__":
    # Run Web Server in background
    Thread(target=run_web).start()
    # Run Trading Engine
    start_bot()
