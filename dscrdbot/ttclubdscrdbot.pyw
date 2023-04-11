import discord
import pyautogui
import win32com.client
from discord.ext import tasks, commands

token = 'PUT_YOUR_TOKEN_HERE'
bot = commands.Bot(command_prefix='!')

@bot.command()
async def start(ctx):
    embed = discord.Embed(title="Местный сторож.", description="Слежу за тем, чтобы все осталось на месте.",
                          color=0xee657)

    await ctx.send(embed=embed)

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
            embed = discord.Embed(title="Местный сторож.",
                                  description="USB СНОВА ПОДКЛЮЧЕН (на ПК №40 в VIP №2)",
                                  color=0xee657)

            await ctx.send(embed=embed)
            error_status = False
        else:
            if not error_status:
                embed = discord.Embed(title="Местный сторож.",
                                      description="ВНИМАНИЕ! На компьютере ОТКЛЮЧИЛСЯ USB! (на ПК №40 в VIP №2)",
                                      color=0xff0000)
                pic = pyautogui.screenshot(r"d:\screenshot.png")
                file = discord.File("d:\screenshot.png", filename="screenshot.png")
                await ctx.send(embed=embed)
                await ctx.send("content", file=file)
                error_status = True

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Местный сторож.", description="Следит, чтобы ничего не попиздили.", color=0xee657)

    embed.add_field(name="Author", value="TTClub Admins")

    await ctx.send(embed=embed)

@commands.command()
async def hi(ctx):
    await ctx.send('Приветствую, Админ! Чтобы начать слежку за устройствами, напиши !start')

@commands.command()
async def status(ctx):
    await ctx.send('Ол гуд!')

bot.add_command(hi)
bot.add_command(status)

bot.run(token)