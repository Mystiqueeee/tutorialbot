import discord
import random
from discord.ext import commands, tasks
from random import choice

client = commands.Bot(command_prefix='*')

status = ['hunting', 'cooking', 'eating']
queue = []

@client.event
async def on_ready():
    change_status.start()
    print('The bot is Online')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))    


client.run('NzcwMDkxMjc5MTUyNzA5NjQy.X5YhZA.kUNFF30kiishyCVWJXpF2E2kLU4')    
