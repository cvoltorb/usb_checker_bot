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

    import win32com.client

    usbs = []
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_USBHub"):
        usbs.append(usb)

    print(usbs)
    print(len(usbs))

    error_status = False

    while True:
        chk_usb = []
        for usb in wmi.InstancesOf("Win32_USBHub"):
            chk_usb.append(usb)
        if len(chk_usb) >= len(usbs) and (not error_status):
            continue
        elif len(chk_usb) >= len(usbs) and error_status:
            bot.send_message(message.chat.id, "USB СНОВА ПОДКЛЮЧЕН на Админском компьютере")
            error_status = False
        else:
            if not error_status:
                bot.send_message(message.chat.id, "💢💥ОШИБКА, USB ОТКЛЮЧЕН на Админском компьютере!💥💢")
                error_status = True


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Я буду сообщать тебе, если у компьютеров в зале что-либо отключится. Для начала сканирования напиши /check".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')

# RUN
bot.polling(none_stop=True)
