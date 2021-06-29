import telebot
from telebot.types import Chat


bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['start'])
def send_text(messages):
    bot.send_message[messages.chat.id, 'Assalomu alaykum']

bot.polling(none_stop=True)