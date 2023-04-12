import requests
import win32com.client

computer_id = 'Админском'

def telegram_bot_sendtext(bot_message):
    bot_token = 'PUT_YOUR_TOKEN_HERE'
    bot_chatID = '723227232'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()


usbs = []
wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf("Win32_USBHub"):
    usbs.append(usb)
error_status = False

while True:
    chk_usb = []
    for usb in wmi.InstancesOf("Win32_USBHub"):
        chk_usb.append(usb)
    if len(chk_usb) >= len(usbs) and (not error_status):
        continue
    elif len(chk_usb) >= len(usbs) and error_status:
        telegram_bot_sendtext("USB СНОВА ПОДКЛЮЧЕН на " + computer_id + " компьютере")
        error_status = False
    else:
        if not error_status:
            telegram_bot_sendtext("💢💥ОШИБКА, USB ОТКЛЮЧЕН на " + computer_id + " компьютере!💥💢")
            error_status = True