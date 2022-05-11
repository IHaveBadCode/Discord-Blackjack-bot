import BankMethods, Blackjack
import os, discord
from KeepAlive import keep_alive
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == os.environ['GUILD']:
      guild = guild.name
      break
    print(f'{bot.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    try:
      file = open(f"Banks/{guild.name}.json", "x")
      file.write("{}")
      file.close()
    except FileExistsError:
      pass
    BankMethods.NewUsers(guild.members)

@bot.command(name='bj', help='Plays Blackjack')
async def BJ(ctx, bet=0):
  try:
    if bet >= 100:
      await Blackjack.Start(bot, ctx, bet)
    elif bet == 0:
      await ctx.reply("smh. You need to bet something, seems like common sense tbh.")
    else:
      await ctx.reply("You cant bet less that **100 coins**, smh")
  except ValueError:
    await ctx.reply("smh. You need to bet something, seems like common sense tbh.")
    
keep_alive()
bot.run(os.environ['TOKEN'])