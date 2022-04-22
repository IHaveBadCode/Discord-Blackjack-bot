import random

class PlayingCards():
  def __init__(self,Deck):
    self.Deck = Deck

  def GetCard(self, num=1):
    Card = self.Deck[0:num] 
    self.Deck = self.Deck[num:]
    return Card

class Player(PlayingCards):
  def __init__(self):
    super().__init__(random.sample(range(52),52))
    self.Hand = self.GetCard(2)
    # self.Hand = [9,51]

  def DrawCard(self):
    self.Hand.append(self.GetCard()[0])

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

  def DisplayHand(self):
    print(self.Hand)

P1 = Player()
# print(P1.Hand)
# print(P1.ModHand())
# print(P1.FullHandTotal())
# P1.DrawCard()
# print(P1.Hand)
# print(P1.ModHand())
# print(P1.FullHandTotal())