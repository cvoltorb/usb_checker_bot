import discord
import win32com.client

token = 'PUT_YOUR_TOKEN_HERE'
bot = commands.Bot(command_prefix='!')

usbs = []
wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.InstancesOf("Win32_USBHub"):
    usbs.append(usb)

print(usbs)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(674880045101219840)
    await channel.send('gg')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send('Приветствую, Админ!')
    elif message.content.startswith('!status'):
        await message.channel.send('Ол гуд!')
    elif message.content.startswith('!help'):
        await message.channel.send('Nope.')
    elif True:
        await message.channel.send('Wha?')


async def background():
    await client.wait_until_ready()

    error_status = False
    while not client.is_closed:
        chk_usb = []
        for usbb in wmi.InstancesOf("Win32_USBHub"):
            chk_usb.append(usbb)
        if len(chk_usb) >= len(usbs) and (not error_status):
            continue
        elif len(chk_usb) >= len(usbs) and error_status:
            await message.channel.send("USB СНОВА ПОДКЛЮЧЕН на Админском компьютере")
            error_status = False
        else:
            if not error_status:
                await message.chanel.send("💢💥ОШИБКА, USB ОТКЛЮЧЕН на Админском компьютере!💥💢")
                error_status = True


client.loop.create_task(background())

client.run(token)
