import os, discord
from discord.ext import commands
import json
import colorama
from colorama import Fore
 
starve = commands.Bot(command_prefix=commands.when_mentioned_or("?"))
os.system('cls')
os.system(f'title [runt (runt#0001)]')
os.system(f'mode 60,20')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
msg = config.get('msg')


@starve.event
async def on_ready():
  print(f""" {Fore.RED}
                               $$\     
                               $$ |    
 $$$$$$\  $$\   $$\ $$$$$$$\ $$$$$$\   
$$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|  
$$ |  \__|$$ |  $$ |$$ |  $$ | $$ |    
$$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ 
$$ |      \$$$$$$  |$$ |  $$ | \$$$$  |
\__|       \______/ \__|  \__|  \____/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
""")


@starve.event
async def on_message(message):
    channel = message.channel
    if message.content.endswith(msg):

        await message.channel.send ('lemme lick all over you')
        await message.channel.send ('lemme finger that nice pussy')
        await message.channel.send ('oh im so hard😼')
        await message.channel.send ('show me how fat that ass is')
        await message.channel.send ('you fucking slut😼')
starve.run(token, bot=False)