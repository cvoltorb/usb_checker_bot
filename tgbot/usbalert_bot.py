import telebot
from telebot import apihelper

token = 'PUT_YOUR_TOKEN_HERE'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Привет Админ ✌!\n Я- <b>{1.first_name}</b>, супер Бот из Cyber Zone TT Club. Я слежу за перефирией игровых компьютеров👁‍🗨. Напиши /help для подробной информации⚠".format(
                         message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['check'])
def checking(message):
    bot.send_message(message.chat.id,
                     "Начал слежку за перефирией игровых ПК😎".format(
                        message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Я буду сообщать тебе, если у компьютеров в зале что-либо отключится. Для начала сканирования напиши /check".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')

# RUN
bot.polling(none_stop=True)
