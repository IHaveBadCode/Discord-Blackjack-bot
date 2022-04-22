import os, BlackJack, discord
from discord.ext import commands
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name ==  os.environ['GUILD']:
      guild=guild.name
      break
    print(
      f'{bot.user} is connected to the following guild:\n'
      f'{guild.name}(id: {guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='bj', help='Plays Blackjack')
async def Blackjack(ctx):
  pass

@bot.command(name='ub', help='Adds new uses to Bank')
async def UpdateBank(ctx):
  for member in ctx.guild.members:
    print(member.id)

bot.run(os.environ['TOKEN'])