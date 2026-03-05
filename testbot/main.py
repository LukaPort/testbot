import telebot
import webbrowser

bot = telebot.TeleBot('8337255076:AAG9vb6QM6oc2BLyMVufJ2pY4NDcxsiQwck')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://funpay.com')

@bot.message_handler(commands=['start','main','hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>No</b> <em><u>help.</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, 'Fuck you')

bot.infinity_polling()