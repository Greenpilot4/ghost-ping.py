from discord.ext import commands
from colorama import Fore, init
import json
import time

init()

with open('token.json') as f:
    data = json.load(f)
token = data['token']

print(Fore.RED + """\
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║  ███╗███████║██║   ██║███████╗   ██║   
██║   ██║██╔══██║██║   ██║╚════██║   ██║   
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                
""" + Fore.RESET)

bot = commands.Bot(command_prefix=".", self_bot=True)

victim = input("Please enter who you would like to ping: ")
victimChannel = int(input("Please enter where you would like to ping (channel ID): "))
pingInterval = int(input("Please enter how often you would to ping (in seconds): "))
repeats = int(input("Please enter how many times you would like to ping: "))

@bot.event
async def on_ready():
    counter = 0
    while counter < repeats:
        channel = bot.get_channel(victimChannel)
        user = "<" + victim + ">"
        msg = await channel.send(user)
        await msg.delete()
        time.sleep(pingInterval)
        counter += 1

bot.run(token, bot=False)

