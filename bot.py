# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has connected to guild {guild.name} (id:{guild.id})')
    print(guild.members)


def sponge(s):
    return ''.join(c.lower() if i % 2 == 1 else c for i, c in enumerate(s.upper()))

# detector de palabrotas
@bot.event
async def on_message(message):
    print(message.author)
    if message.author == bot.user:
        return
    if "puto" in str(message.content).lower():
        response = "ANDA A LAVARTE LA BOCA CON AGUA Y JABON!"
        await message.channel.send(response)
    
    if str(message.author) == "lhninethree#7551":
        response = sponge(message.content)
        await message.channel.send(response)

    if str(message.author) == "hongosupremo#4805":
        response = f'El supremo sama ha hablado.\n El gran sama dijo:"{message.content}"'
        await message.channel.send(response)
    await bot.process_commands(message)


@bot.command(name='supremo_sama', help='te dice quien es el rey')
async def supremosama(ctx):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    for member in guild.members:
        print(member)
        if member.name not in ["testbot","8CHOBOT","Gnar"]:
            await member.send(
                f'Hola {member.name}, este es el universo recordandote que Samuel Hong es el supremo-sama.\n Besitos 😘')

bot.run(TOKEN)
