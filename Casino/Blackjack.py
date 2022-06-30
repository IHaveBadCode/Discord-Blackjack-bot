import random, discord, Methods, BankMethods
import Componants.BJ as BJ
from threading import Thread
# https://discordpy.readthedocs.io/en/latest/interactions/api.html?highlight=compo#button
# 🎰   🎁   🍺   ✨   💰   🍀




class PlayingCards():
  def __init__(self, deck):
    self.Deck = deck

  def DealCard(self, num=1):  
    Card = self.Deck[0:num] 
    self.Deck = self.Deck[num:]
    return Card

class Player():
  def __init__(self, ctx, AllCards, bet, Dealer=None, embed=None):
    self.AllCards=AllCards
    self.Dealer = Dealer
    self.embed = embed
    self.ctx = ctx
    self.Hand = AllCards.DealCard(2)
    self.bet = bet

  def PrettyCards(self):
    Suit={ 
      0:"\u2664",
      1:"\u2667",
      2:"\u2662",
      3:"\u2661"}
    FaceCards={
      1:"A",
      11:"J",
      12:"K",
      13:"Q"}
        
    temp0 =[FaceCards[B] if B==1 or B==11 or B==12 or B==13 else B for B in self.ModHand()]
    temp1 =[Suit[A//13] for A in self.Hand]
    temp2 = []
    for i in range(len(self.Hand)):
      temp2.append(f"{temp1[i]} {temp0[i]}")
    return temp2
    
  async def DrawCard(self, index=0):
    self.Hand.append(self.AllCards.DealCard()[0])
    self.embed.FieldEdit(f"{self.embed.ctx.author.name} (Player)", f"Cards - {self.PrettyCards()} \n Total - {self.HandTotal()}",0)
    self.embed.FieldEdit(f"Great Code (Dealer)", f"Cards - {self.Dealer.PrettyCards()} \n Total - {self.Dealer.HandTotal()}",1)
    await self.embed.CommitEdit()
    
  def ModHand(self):
    Temp = [(x+1) % 13 for x in self.Hand]# converts from 1-52 to 0-12
    return Temp
    
  def HandTotal(self):
    Temp = self.ModHand()
    Temp[:] = [10 if A>=10 else A for A in Temp]# defines picture cards of value 10
    Temp[:] = [11 if B==0 else B for B in Temp]# defines ace as value 11
    for x in range(Temp.count(11)):
      if sum(Temp)>21:
        Temp.append(-10)
    return sum(Temp)
  async def Stand(self):
    self.embed.FieldInsert("The Dealer is drawing",
                        f"the dealer is drawing cards you are too afraid to draw",
                        0,
                        False)
    self.embed.ColorSet(discord.Color.orange())
    await self.embed.CommitEdit()

  async def Forefit(self):
    self.embed.FieldInsert("You ended the game.",
                        f"The dealer is keeping your money to deal with your bullcrap.",
                        0,
                        False)
    self.embed.ColorSet(discord.Color.orange())
    await self.embed.CommitEdit()
    
  def DoubleDown(self):
    pass
  def SplitHands(self):
    pass
  def Insurance(self):
    print("insiururu")


async def Start(bot, ctx, bet):
  AllCards = PlayingCards(random.sample(range(0,52), 52))
  embed = Methods.Embeds(bot, ctx)
  dealer = Player(ctx, AllCards, 0)
  player = Player(ctx, AllCards, 0, dealer, embed)

  # class Buttons(discord.ui.View):
  #     def __init__(self, *, timeout=180):
  #         super().__init__(timeout=timeout)
  #     @discord.ui.button(label="Hit",style=discord.ButtonStyle.green, row=0)
  #     async def Hit_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       await player.DrawCard()
  #     @discord.ui.button(label="Stand",style=discord.ButtonStyle.green, row=0)
  #     async def Stand_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       self.DisableAllButtons()
  #       await player.Stand()
  #     @discord.ui.button(label="Forefit", style=discord.ButtonStyle.red, row=0)
  #     async def Forefit_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       self.DisableAllButtons()
  #       await player.Forefit()
  #     @discord.ui.button(label="DoubleDown",style=discord.ButtonStyle.blurple, row=1)
  #     async def DoubleDown_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       player.DoubleDown()
  #     @discord.ui.button(label="SplitHands",style=discord.ButtonStyle.blurple, row=1)
  #     async def SplitHand_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       player.SplitHands()
  #     @discord.ui.button(label="Insurance",style=discord.ButtonStyle.blurple, row=1)
  #     async def Insurance_button(self, button:discord.ui.Button, interaction:discord.Interaction):
  #       player.Insurance() 
        
  #     def DisableButton(self, label, state):
  #       for child in self.children:
  #         if child.label==label:
  #           child.disabled=state
            
  #     def DisableAllButtons(self):
  #       for child in self.children:
  #         child.disabled=True
  
  
  veiw=BJ.Buttons()
  embed.Create()
  embed.DisplayNameSet(f"{ctx.author.name}'s Blackjack game")
  embed.FieldAdd(f"{ctx.author.name} (Player)", f"Cards - {player.PrettyCards()} \n Total - {player.HandTotal()}")
  embed.FieldAdd(f"Great Code (Dealer)", f"Cards - {dealer.PrettyCards()} \n Total - {dealer.HandTotal()}")
  embed.FooterSet("K, Q, J = 10  |  A = 1 or 11")
  embed.ColorSet(discord.Color.from_rgb(3, 102, 252))
  if player.HandTotal() != 9 or 10 or 11:#double down # or if not enough in waller to do double down
    veiw.DisableButton("DoubleDown", True)
  if player.ModHand()[0] != player.ModHand()[1]:#split hands
    veiw.DisableButton("SplitHands", True)
  if dealer.ModHand()[1] != 0:#Insurance
    veiw.DisableButton("Insurance", True)

  
  await embed.Send(veiw)