import ccxt
import time
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "OKX Sniper Bot is Active"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# بيانات الـ API الجديدة الخاصة بك
params = {
    'apiKey': '0850a1b5-d861-4874-8d17-cb50d9e6ea19',
    'secret': '4AD2FC402C6204F1B4489DE2F9053F02',
    'password': 'asdFF124$',
    'enableRateLimit': True,
}

exchange = ccxt.okx(params)
# استخدام خادم السحاب لتجاوز أي حجب إقليمي
exchange.urls['api']['public'] = 'https://aws.okx.com'
exchange.urls['api']['private'] = 'https://aws.okx.com'

symbol = 'PEPE/USDT:USDT'

def start_bot():
    print("🚀 Starting Bot on Cloud Server...")
    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            print(f"💰 PEPE Price: {price}")
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Reconnecting... Error: {e}")
            time.sleep(20)

if __name__ == "__main__":
    # تشغيل السيرفر لضمان بقاء Render نشطاً
    threading.Thread(target=run_web).start()
    # تشغيل محرك البوت
    start_bot()
