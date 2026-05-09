import ccxt
import time
from flask import Flask
from threading import Thread

# تشغيل سيرفر ويب لضمان استمرار الخدمة مجانية
app = Flask('')
@app.route('/')
def home(): return "Pepe Sniper Bot is Running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# إعدادات الحساب (بياناتك الفعلية)
params = {
    'apiKey': '9a3d6d8a-065c-4d1a-9073-db0ed6473ebd',
    'secret': 'A6B6C16AC035262F8B840052D9916B7B',
    'password': 'asdFF124$',
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
}

ex = ccxt.okx(params)
symbol = 'PEPE-USDT-SWAP'
amount = 1000000 

def sniper_logic():
    print("🎯 قناص PEPE الذكي بدأ العمل..")
    while True:
        try:
            ticker = ex.fetch_ticker(symbol)
            price = float(ticker['last'])
            print(f"📊 السعر الحالي: {price:.8f}")
            
            # فتح صفقة شراء
            # order = ex.create_market_buy_order(symbol, amount)
            
            time.sleep(20)
        except Exception as e:
            print(f"🔄 خطأ: {e}")
            time.sleep(30)

if __name__ == "__main__":
    Thread(target=run_web).start()
    sniper_logic()
