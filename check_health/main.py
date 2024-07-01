from flask import Flask, request
import telebot

app = Flask(__name__)

# ССЫЛКА НА БОТА
# https://t.me/HealtServices_checker_bot
bot = telebot.TeleBot('7473902988:AAEsFekyyT-s0j4Bt4JVt4iX37MDMHLI6kk')


@app.route('/notify', methods=['POST'])
def notify():
    data = request.data.decode('utf-8')
    if data:
        message = data
        chat_id = '892556581'   
        bot.send_message(chat_id, message)
        return 'Notification sent', 200
    else:
        return 'Invalid request', 400


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hello")


if __name__ == '__main__':
    app.run(host='localhost', port=9001, debug=True)
    bot.polling(non_stop=True)