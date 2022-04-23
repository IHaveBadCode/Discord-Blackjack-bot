import BankMethods, BlackJack
import os, discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
DiscordComponents(bot)

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == os.environ['GUILD']:
      guild=guild.name
      break
    print(
      f'{bot.user} is connected to the following guild:\n'
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
async def Blackjack(ctx):
  BlackJack.InitiateBJ(ctx)

@bot.command()
async def hello(ctx):
  await ctx.send("hello", components=[
    [Button(label="Hi",style="3",custom_id="button1"), Button(label="Bye",style="4",custom_id="button2")]
  ])
  interaction = await bot.wait_for("button_click", check= lambda i: i.custom_id == "button1")
  await interaction.send(content = "Button clicked!", ephemeral=True)




class Embeds():
  def __init__(self, ctx):
    self.embed = None
    self.msg = None
    self.ctx = ctx


  def Create(self):
    self.embed = discord.Embed()
    self.embed.set_author(
      name = f"{self.ctx.author.display_name}'s", 
      icon_url = self.ctx.author.avatar_url,
      url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  def SetDisplayName(self, name):
    self.embed.set_author(
      name = name,
      icon_url = self.ctx.author.avatar_url,
      url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  
  def AddField(self, name, value, inline=False):
    self.embed.add_field(
      name=name, 
      value=value, 
      inline=inline)

  def RemoveField(self, index=0):
    self.embed.remove_field(index=index)
    
  def SetFooter(self, footer):
    self.embed.set_footer(text=footer)

  def SetDesc(self, desc):
    self.embed.description = desc
  
  def SetColor(self, color):
    self.embed.color=color
    
  async def Send(self):
    self.msg = await self.ctx.send(embed=self.embed)

  async def CommitEdit(self):
    await self.msg.edit(embed=self.embed)


@bot.command()
async def embed(ctx):
  embed = Embeds(ctx)
  embed.Create()
  embed.AddField("Ha lol", "You poor af boi get good")
  embed.AddField("Player Cards", "noob oyu got none", True)
  embed.AddField("Dealer Cards", "boss man got entire deck", True)
  embed.SetFooter("A=11/1  J/Q/K=10")
  embed.SetColor(discord.Color.red())
  await embed.Send()
  await embed.CommitEdit()
  # embed.RemoveField()
  # await embed.Send()
  # time.sleep(1)
  # embed.title = None
  # await embed.CommitEdit()

  # color=discord.Color.blue())


bot.run(os.environ['TOKEN'])