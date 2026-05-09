import ccxt
import time
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "OKX Bot is Online"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# API Info from your last image
params = {
    'apiKey': '0850a1b5-d861-4874-8d17-cb50d9e6ea19',
    'secret': '4AD2FC402C6204F1B4489DE2F9053F02',
    'password': 'asdFF124$',
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
}

exchange = ccxt.okx(params)
symbol = 'PEPE/USDT:USDT'

def start_bot():
    print("🚀 Bot process started...")
    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            print(f"💰 LIVE PRICE: {price}")
            
            # أمر شراء تجريبي بسيط جداً إذا أردت التأكد من التداول
            # سنكتفي بالطباعة أولاً للتأكد من الاتصال
            
            time.sleep(5)
        except Exception as e:
            print(f"⚠️ Connection Issue: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # تشغيل السيرفر لضمان عدم توقف Render
    t = threading.Thread(target=run_web)
    t.start()
    # تشغيل البوت فوراً
    start_bot()
