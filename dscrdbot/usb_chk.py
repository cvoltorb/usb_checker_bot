import win32com.client

computer_id = 'Админском'

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
        ("USB СНОВА ПОДКЛЮЧЕН на " + computer_id + " компьютере")
        error_status = False
    else:
        if not error_status:
            ("💢💥ОШИБКА, USB ОТКЛЮЧЕН на " + computer_id + " компьютере!💥💢")
            error_status = True