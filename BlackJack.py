import random

class PlayingCards():
  def __init__(self,Deck):
    self.Deck = Deck

  def DealCard(self, num=1):
    Card = self.Deck[0:num] 
    self.Deck = self.Deck[num:]
    return Card

class Player(PlayingCards):
  def __init__(self):
    super().__init__(random.sample(range(52),52))
    self.Hand = self.DealCard(2)

  def DrawCard(self):
    self.Hand.append(self.DealCard()[0])

  def ModHand(self):
    Temp = [(x+1) % 13 for x in self.Hand]# converts from 1-52 to 0-12
    return Temp
    
  def FullHandTotal(self):
    Temp = self.ModHand()
    Temp[:] = [10 if A>=10 else A for A in Temp]# defines picture cards of value 10
    Temp[:] = [11 if B==0 else B for B in Temp]# defines ace as value 11
    while sum(Temp)>21 and Temp.count(11)>=1:
      Temp.append(-10)
    return sum(Temp)

  def Bet(self):
    Bet = int(input("how much do you want to bet"))
    #need to make the bet actually do something
    self.StartGame()
  def StartGame(self):
    pass

def InitiateBJ(member):
  pass