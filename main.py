from discord.ext import commands
from colorama import Fore, init
import json
import asyncio
import os

if os == "Windows":
    init()

with open('token.json') as f:
    data = json.load(f)

token = data['token']
bot = commands.Bot(command_prefix="*!*", self_bot=True)

async def main():
    if os == "Windows":
        system("cls")
    else:
        system("clear")
    print(chr(27) + "[2J")
    print(Fore.LIGHTRED_EX + """\n
     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██╗███╗   ██╗ ██████╗ 
    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║████╗  ██║██╔════╝ 
    ██║  ███╗███████║██║   ██║███████╗   ██║       ██████╔╝██║██╔██╗ ██║██║  ███╗
    ██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██╔═══╝ ██║██║╚██╗██║██║   ██║
    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██║     ██║██║ ╚████║╚██████╔╝
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝               
    """ + Fore.LIGHTYELLOW_EX)

    victim = str(input("[-] User to ping: "))
    victimChannel = int(input("[-] Message channel: "))
    repeats = int(input("[-] Ping repeats: "))
    if repeats > 1:
        pingInterval = int(input("[-] Ping interval: "))
    else:
        pingInterval = 0
    pingmessage = input("[-] Message (Press enter for no message): ")
    deletemessageInput = input("[-] Ghost ping?: ")

    if pingmessage == "":
        pingmessage = None
        pingmessageBool = False
    else:
        pingmessageBool = True

    if deletemessageInput == "yes" or deletemessageInput == "y":
        deletemessageBool = True
    else:
        deletemessageBool = False


    if victim == "@everyone" or victim == "everyone":
        user = "@everyone"
    elif len(victim) == 18:
        user = "<" + "@" + victim + ">"
    elif len(victim) == 19:
        user = "<" + victim + ">"
    else:
        print(Fore.RED + "Invalid User!")
    await pingg(user, victimChannel, pingInterval, repeats, pingmessage, pingmessageBool, deletemessageBool)

async def pingg(user, victimChannel, pingInterval, repeats, pingmessage, pingmessageBool, deletemessageBool):
    counter = 0
    print(Fore.LIGHTCYAN_EX + "\n[*] Pinging..\n")
    while counter != repeats:
        channel = bot.get_channel(victimChannel)
        if pingmessageBool == True:
            charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
            msg = await channel.send(pingmessage + charTT + user)
            if deletemessageBool == True:
                await msg.delete()
        else:
            msg = await channel.send(user)
            if deletemessageBool == True:
                await msg.delete()

        counter += 1
        print(Fore.CYAN + "[+] Pinged " + str(counter) + " time(s)..")

        if counter == repeats:
            print(Fore.LIGHTYELLOW_EX + "\n[+] All done!")
            await main()

        await asyncio.sleep(pingInterval)

@bot.event
async def on_ready():
    await main()

bot.run(token, bot=False)
