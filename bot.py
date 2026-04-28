import telebot
import requests

# ضع التوكن الخاص بك هنا
TOKEN = '8728709789:AAGnMRdSRK8UPVRdrX8Kpgua4eotLv09HrY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🌟 أهلاً بك في بوت التحميل الأسطوري!\nفقط أرسل رابط فيديو تيك توك وسأرسله لك بدون علامة مائية فوراً.")

@bot.message_handler(func=lambda m: 'tiktok.com' in m.text)
def download_tiktok(message):
    msg = bot.reply_to(message, "⏳ جاري جلب الفيديو... انتظر ثواني")
    try:
        url = message.text
        # استخدام API خارجي سريع ومجاني
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        
        video_url = response['data']['play'] # فيديو بدون علامة مائية
        title = response['data'].get('title', 'تم التحميل بواسطة بوتك الأسطوري')
        
        bot.send_video(message.chat.id, video_url, caption=f"✅ تم التحميل بنجاح:\n{title}")
        bot.delete_message(message.chat.id, msg.message_id)
    except Exception as e:
        bot.edit_message_text("❌ حدث خطأ! تأكد من أن الرابط صحيح أو حاول مرة أخرى.", message.chat.id, msg.message_id)

print("--- البوت شغال الآن على السيرفر ---")
bot.polling(non_stop=True)
