suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
import random



class Card():
    
    #atributrs for type and value
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        
        return self.rank + " of " + self.suit




class Deck():
    """docstring for Deck"""
    def __init__(self):

        
        self.deck = []
        for x in suits:
            for y in ranks:
                self.deck.append(Card(x,y))
                
    def shuf(self):
        random.shuffle(self.deck)
        
    def __str__(self):
            for x in self.deck:
                print(x)
            return 0
        
test = Deck
test.shuf()













mydeck = Deck
#mydeck.shuf()
print(list(mydeck.deck))



