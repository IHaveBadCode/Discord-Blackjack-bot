import BankMethods, BlackJack, time
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
  def __init__(self, ctx, title, desc, color, footer):
    self.embed = None
    self.msg = None
    
    self.ctx = ctx
    self.title = title
    self.desc = desc
    self.color = color
    self.footer = footer

    self.Author_Name = ctx.author.display_name
    self.Author_Icon = ctx.author.avatar_url

  def Create(self):
    self.embed=discord.Embed(
      title=self.title, 
      description=self.desc, 
      color=self.color)
      # color=discord.Color.blue())
  
    self.embed.set_author(
      name = self.ctx.author.display_name, 
      icon_url= self.Author_Icon)

    self.embed.add_field(name="You didn't respond in time.", value="The dealer is keeping your money to deal with your bullcrap", inline=False)
    self.embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
    self.embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
    self.embed.set_footer(text=self.footer)
    
  async def Send(self):
    self.Create()
    self.msg = await self.ctx.send(embed=self.embed)

  async def CommitEdit(self):
    self.Create()
    await self.msg.edit(embed=self.embed)


@bot.command()
async def embed(ctx):
  embed = Embeds(ctx,"hello", "*You didn't respond in time.", discord.Color.blue(), "A=11/1 K/Q/J=10")
  await embed.Send()
  time.sleep(1)
  embed.title = None
  await embed.CommitEdit()

  


bot.run(os.environ['TOKEN'])