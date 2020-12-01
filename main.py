from discord.ext import commands
from colorama import Fore, init
import json
import asyncio

init()

with open('token.json') as f:
    data = json.load(f)
token = data['token']

print(Fore.RED + """\
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║████╗  ██║██╔════╝ 
██║  ███╗███████║██║   ██║███████╗   ██║       ██████╔╝██║██╔██╗ ██║██║  ███╗
██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██╔═══╝ ██║██║╚██╗██║██║   ██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██║     ██║██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝               
""" + Fore.RESET)

bot = commands.Bot(command_prefix="*!*", self_bot=True)

victim = str(input("Please enter who you would like to ping: "))
victimChannel = int(input("Please enter where you would like to ping (channel ID): "))
pingInterval = int(input("Please enter how often you would to ping (in seconds): "))
repeats = int(input("Please enter how many times you would like to ping: "))

if victim == "@everyone" or victim == "everyone":
    user = "@everyone"
elif len(victim) == 18:
    user = "<" + "@" + victim + ">"
elif len(victim) == 19:
    user = "<" + victim + ">"
else:
    print("Invalid User!")

@bot.event
async def on_ready():
    counter = 0
    while counter < repeats:
        channel = bot.get_channel(victimChannel)
        msg = await channel.send(user)
        await msg.delete()
        await asyncio.sleep(pingInterval)
        counter += 1

bot.run(token, bot=False)

