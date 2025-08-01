from flask import Flask, request
import telebot

API_TOKEN ='8257588830:AAFHvRCKpQsD9coxnGNFQ7wbYG9icoPVn54'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بك في بوت Aviator!")

@app.route(f"/{API_TOKEN}", methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def index():
    return "البوت شغال ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
