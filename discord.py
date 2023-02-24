import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, {0.author.mention}!'.format(message))

TOKEN = '🐺🐺🐺🐺'

if not TOKEN:
    print('Error: Discord token not found.')
else:
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print('Error: Invalid Discord token.')
