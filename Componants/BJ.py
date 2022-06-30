import discord

class Buttons(discord.ui.View):
      def __init__(self, *, timeout=180, Player):
          super().__init__(timeout=timeout)
          self.player=Player
      @discord.ui.button(label="Hit",style=discord.ButtonStyle.green, row=0)
      async def Hit_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        await self.player.DrawCard()
      @discord.ui.button(label="Stand",style=discord.ButtonStyle.green, row=0)
      async def Stand_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        self.DisableAllButtons()
        await self.player.Stand()
      @discord.ui.button(label="Forefit", style=discord.ButtonStyle.red, row=0)
      async def Forefit_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        self.DisableAllButtons()
        await self.player.Forefit()
      @discord.ui.button(label="DoubleDown",style=discord.ButtonStyle.blurple, row=1)
      async def DoubleDown_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        self.player.DoubleDown()
      @discord.ui.button(label="SplitHands",style=discord.ButtonStyle.blurple, row=1)
      async def SplitHand_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        self.player.SplitHands()
      @discord.ui.button(label="Insurance",style=discord.ButtonStyle.blurple, row=1)
      async def Insurance_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        self.player.Insurance() 
        
      def DisableButton(self, label, state):
        for child in self.children:
          if child.label==label:
            child.disabled=state
            
      def DisableAllButtons(self):
        for child in self.children:
          child.disabled=True
  