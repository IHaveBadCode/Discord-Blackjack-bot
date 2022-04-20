import json, random

class PlayingCards():
  def __init__(self,Deck):
    self.Deck = Deck

  def GetCard(self):
    Card = self.Deck[0]
    self.Deck.remove(Card)
    return Card
    
p1 = PlayingCards([1,2,3,4])

class Player():
  def __init__(self):
    self.hand = []
    
  def DrawCard(self):
    self.hand.append(p1.GetCard())
    

p2 = Player()
p2.DrawCard()
    