from discord.ext import commands
from colorama import Fore, init
import json
import asyncio
import os

init()
with open('token.json') as f:
    data = json.load(f)

token = data['token']
bot = commands.Bot(command_prefix="*!*", self_bot=True)

async def main():
    os.system('cls')
    print(Fore.RED + """\
     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██╗███╗   ██╗ ██████╗ 
    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║████╗  ██║██╔════╝ 
    ██║  ███╗███████║██║   ██║███████╗   ██║       ██████╔╝██║██╔██╗ ██║██║  ███╗
    ██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██╔═══╝ ██║██║╚██╗██║██║   ██║
    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██║     ██║██║ ╚████║╚██████╔╝
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝               
    """ + Fore.RESET)
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
    await pingg(user, victimChannel, pingInterval, repeats)
    return

async def pingg(user, victimChannel, pingInterval, repeats):
    counter = 0
    while counter != repeats:
        channel = bot.get_channel(victimChannel)
        msg = await channel.send(user)

        await msg.delete()
        await asyncio.sleep(pingInterval)
        counter += 1
        print("Pinged " + str(counter) + " time(s)..")
        if counter == repeats:
            print("All done!")
            await main()
    return

@bot.event
async def on_ready():
    await main()
    return

bot.run(token, bot=False)