import win32com.client

usbs = []
wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf("Win32_USBHub"):
    usbs.append(usb)
error_status = False

print(usbs)

while True:
    chk_usb = []
    for usb in wmi.InstancesOf("Win32_USBHub"):
        chk_usb.append(usb)
    if len(chk_usb) >= len(usbs) and (not error_status):
        continue
    elif len(chk_usb) >= len(usbs) and error_status:
        print("USB СНОВА ПОДКЛЮЧЕН")
        error_status = False
    else:
        if not error_status:
            print("ОШИБКА, USB ОТКЛЮЧЕН!")
            error_status = True