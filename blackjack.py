suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
import random



class Card:
    
    #atributrs for type and value
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        
        return self.rank + " of " + self.suit


class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        lst =[]
        for i in self.deck:
            lst.append(str(i))
        return str(lst)
         

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card1 = self.deck.pop(0)
        card2 = self.deck.pop(0)
        return card1, card2




class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        if len(self.cards) == 3:
            self.cards.pop()
            
        self.cards+= card
        
    
    def adjust_for_ace(self):
        
        for card in self.cards:
            self.value+= card.value
            if card.value == 11 :
                self.aces+= 1
                
        
        while self.value <= 21  or self.aces == 0 :
            self.value-= 10 
            self.aces-= 1
            

class Chips:
    
    def __init__(self):
        
        self.total = int(input("enter the chips you want to buy"))  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self, bet):
        self.total+= bet
        self.bet = 0
        
    
    def lose_bet(self, bet):
        if bet > self.total:
            print("not enough money")
        else:
            self.total-= bet
        self.bet = 0




def take_bet():
    loop = True
    while loop:
        try:

            bet = int(input("enter the betting amount in digits "))
            loop = False
            
        except :

            print(" wrong input ! ")
            loop = True
    
    return bet

            
            
        
        
    


# In[72]:



def hit(deck,hand):
    hand.add_card(deck.pop(0))
    


# In[73]:



def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        
        key = input(" do you want to hit or stand : ( h/s)")
        if key in ('h','s'):
            break
    if key == 'h':
        hit(deck, hand)
    else:
        playing = False
        
        
        


# In[74]:


def show_some(player,dealer):
    
    print("player cards :")
    for card in player.cards:
        print(card)
    print(" value :", player.value)
    print("-*20")
    print("dealer cards :")
    print(dealer.cards[0])
    
def show_all(player,dealer):
    print("player cards :")
    for card in player.cards:
        print(card)
    print("player value :", player.value)
    
    print("dealer cards :")
    for card in dealer.cards:
        print(card)
    print("dealer value :", dealer.value)
  


# In[75]:


def player_busts():
    print("player is busted ")
    print("player looses")
    

def player_wins():
    
    if player.value > dealer.value :
        print("player wins")
        return True

def dealer_busts():
    if dealer.value >21 :
        print("dealer is busted")
        print("player wins")
        return True
    
def dealer_wins():
    if player.value < dealer.value :
        print("dealer wins")
        return True
    
def push():
    if player.value == dealer.value :
        print("push")
        return True
        


# In[93]:



while True:
    # Print an opening statement
    print(" welcome to BlackJack")
    

    
    # Create & shuffle the deck, deal two cards to each player
    
    playdeck = Deck

    playdeck.shuffle()
    playdeck.shuffle()
    player =Hand
    dealer = Hand
    card1,card2 = playdeck.deal()
    player.add_card(card1, card2)
    card1,card2 = playdeck.deal()
    dealer.add_card(card1, card2)
    player.adjust_for_ace()
    dealer.adjust_for_ace()
    
    

    
        
    # Set up the Player's chips
    player_chips = Chips
    
    
    
    # Prompt the Player for their bet
    bet = take_bet()
    player_chips.lose_bet(bet)
    

    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    playing = True
    
    
    
    hit_or_stand(playdeck.deck,player)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        
        player.add_card(playdeck.deck.pop(0))
        player.adjust_for_ace()
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
         
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts()
            break
        
        hit_or_stand(playdeck.deck,player)
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    while dealer.value > 17:
        dealer.add_card(playdeck.deck.pop(0))
        dealer.adjust_for_ace()
        # Show all cards
    show_all(player,dealer)
    
        # Run different winning scenarios
    if player_wins():
        player_chips.win_bet(bet)
    player_busts()
    dealer_busts()
    dealer_wins()
    push

        
    
    # Inform Player of their chips total 
    print("balance is ", player_chips.total)
    
    # Ask to play again
    if input("play again :(y  / n)") in ['n'] :

        break




