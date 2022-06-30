import discord, asyncio
# from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


class Embeds():
  def __init__(self, bot, ctx):
    # DiscordComponents(bot)
    # self.Components = None
    self.embed = None
    self.msg = None
    self.bot = bot
    self.ctx = ctx

  def Create(self):
    self.embed = discord.Embed()
    self.embed.set_author(
      name = f"hello",
      # name = f"{self.ctx.author.display_name}'s", 
      icon_url = self.ctx.author.avatar,
      url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  def DisplayNameSet(self, name):
    self.embed.set_author(
      name = name,
      # icon_url = self.ctx.author.avatar_url,
      url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

  def ThumbnailSet(self, url):
    self.embed.set_thumbnail(url=url)

  def FieldInsert(self, header, txt, index, inline=True):
    self.embed.insert_field_at(
      name=header, 
      value=txt,
      index=index,
      inline=inline)
    
  def FieldAdd(self, header, txt, inline=True):
    self.embed.add_field(
      name=header, 
      value=txt,
      inline=inline)

  def FieldRemove(self, index=0):
    self.embed.remove_field(index=index)
    
  def FieldEdit(self, header, txt, index, inline= True):
    self.embed.set_field_at(index=index, name=header, value=txt, inline=inline)
  
  def FooterSet(self, footer):
    self.embed.set_footer(text=footer)

  def DescSet(self, desc):
    self.embed.description = desc
  
  def ColorSet(self, color):
    self.embed.color=color  
    
  async def Send(self, Buttons= None):
    self.msg = await self.ctx.send(embed=self.embed, view=Buttons)

  async def CommitEdit(self):
    await self.msg.edit(embed=self.embed)