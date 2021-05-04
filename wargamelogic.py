'''
GAME OF WARS WITH CARD

'''
# generating value for rank of cards

#value = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13 ,'ace':14}
#suit = ['hearts','diamonds','clubs','spades']
from colorama import init
init()
from colorama import Fore, Back, Style



value = {'two':2, 'three':3, 'four':4, 'five':5}
suit = ['hearts','diamonds','clubs',]
# card class for storing card info

class Card():
    
    #atributrs for type and value
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
        
    def __str__(self):
        
        return self.rank + " of " + self.suit

# CREATING A DECK OF CARDS
# WHICH IS A LIST OF 52 CARD ELEMENTS

import random

class Deck():
        def __init__(self):
            
            self.created_cards =[]
    
        def create_deck(self):
            
            # creating a deck fo cards with combination
            # of suits and values
            self.created_cards = []
            for s in suit:
                for val in value.keys():
                    self.created_cards.append(Card(s,val))
        
        def shuffle(self):
        	# shuffling the list of 52 cards
            
            random.shuffle(self.created_cards)


class Player():
    
    # creating a player 
    
    def __init__(self):
        
        # creates a deck of 52 cards for player and
        #saves in player.hand
        
        self.hand = Deck()
        
        # empty hand of card created
        
    def hand(self):
        
        #creating a hand 
        
        self.hand.create_deck()
        self.hand.shuffle
        # a shuffled deck of card will be created at
        #player.hand.created hand 
        

class card_pick():
    
    def pick():
        while True:
            
            key = input("PLAYER 1 : press 5 to take out a card")
            
            if key == '5' :
                hand_one = player1.hand.created_cards.pop(0)
                break
        while True:
            key = input("PLAYER 2 : press 5 to take out a card")
            
            if key == '5' :
                hand_two = player2.hand.created_cards.pop(0)
                break
        
        return hand_one , hand_two






def out(a,b,c):
    x= str(a)
    y= str(b)
    z= str(c)
    print("-"*20, '+', '-'*20, '+', '-'*5,'+')
    print(Fore.YELLOW+Back.WHITE+'|', 'PLAYER 1 ',' '*9,'|','PLAYER 2 ',' '*10,'|','RANK', ' |')
    print(Style.RESET_ALL)
    print(Back.WHITE+"-"*20, '+', '-'*20, '+', '-'*5,'+')
    print(Fore.RED+'|', x,' '*(17 -len(x)),'|',y,' '*(19 - len(y)),'|',z," "*2, ' |')
    print(Back.WHITE+"-"*20, '+', '-'*20, '+', '-'*5,'+')
    print(Style.RESET_ALL)


##### 
# game logic
class gameon():
    
    def call():
        while True:

                 
            game_start = input("Are you ready to play (y/n ) :")
            if game_start in ('y','Y'):
                print(Fore.WHITE+Back.RED+  '-'*10, " GAME BEGINS ", '-'*15)
                print(Style.RESET_ALL)
                print('~'*40)
                print("generating cards for each player ",'^'*20,"success")
                
                return True
                break
            elif game_start in ('N','n'):
                print("Thanks ! \nSee you ")
                return False
                break
            else:
                print("oops!, Try again")
            
                
play = gameon.call()



# print("generating cards for each player ",'^'*20,"success")
player1 = Player()
player2 = Player()
# hands creation
player1.hand.create_deck()
player2.hand.create_deck()
#shuffling

player1.hand.shuffle()
player2.hand.shuffle()
ext = []
lst_card = []
flag = True
count = 0
while  play == True and flag == True:
    
    count+=1
    # checking for empty hand
    #from IPython.display import clear_output
    #clear_output(wait=True)
    #if ext!=[]:
    #hand_one , hand_two = card_pick.pick()
    #lst_card =[hand_one, hand_two]
        
    #else:
    #   ext1 = hand_one
    #    ext2 = hand_two
    #    hand_one,hand_two = card_pick.pick()
    #    lst_card =[hand_one, hand_two,ext1,ext2]
    
    hand_one,hand_two = card_pick.pick()
    
    lst_card+= [hand_one]
    lst_card+= [hand_two]
    out(str(hand_one), str(hand_two), max(hand_one.value, hand_two.value))
    
    
    if hand_one.value != hand_two.value:
        if hand_one.value > hand_two.value:
            
            player1.hand.created_cards+= lst_card
            lst_card =[]
            #if ext!= []:
            #   player1.hand.created_cards+= ext
            #    ext = []
            #from IPython.display import clear_output
            #clear_output(wait=True)
            
            #out(str(hand_one), str(hand_two), hand_one.value)
            
            print("player 1 wins round")
            
        elif hand_one.value < hand_two.value:
            
            player2.hand.created_cards+= lst_card
            lst_card = []
            #if ext!= []:
            #    player2.hand.created_cards+= ext
            #    ext = []
            #from IPython.display import clear_output
            #clear_output(wait=True)
            
            #out(str(hand_one), str(hand_two), hand_two.value)
            print("player 2 wins round")
    else:
        
        print("equal cards ")
        print("next round ")
        out(str(hand_one), str(hand_two), max(hand_one.value, hand_two.value))
        
        

        if len(player1.hand.created_cards) >6 and len(player2.hand.created_cards) >6 :

        

            print("taking 5 cards ")
            #ext = []
            for i in range(5):
                    
                    lst_card += [player1.hand.created_cards.pop(0)]
                    lst_card += [player2.hand.created_cards.pop(0)]
                    print(len(player1.hand.created_cards),' bal for ply1')
                    print(len(player2.hand.created_cards),' bal for ply2')

            continue

        if len(player1.hand.created_cards) >4 and len(player2.hand.created_cards) >4 :

        

            print("taking 3 cards ")
            #ext = []
            for i in range(3):
                    
                    lst_card += [player1.hand.created_cards.pop(0)]
                    lst_card += [player2.hand.created_cards.pop(0)]
                    print(len(player1.hand.created_cards),' bal for ply1')
                    print(len(player2.hand.created_cards),' bal for ply2')
            continue
        if len(player1.hand.created_cards) == 1:

            print('!*50')
            print(Fore.BLUE+Back.WHITE+"PLAYER 2 WINS ")
            print('!'*50)
            break
    
        elif len(player2.hand.created_cards) == 1: 
            print('!*50')
            print(Fore.BLUE+Back.WHITE+"PLAYER 1 WINS ")
            print('!*50')
            break



        
    print("current tally")
    out(len(player1.hand.created_cards) , len(player2.hand.created_cards), '-')
    
    #from IPython.display import clear_output
    #clear_output(wait=True) 
    
            
    if len(player1.hand.created_cards) == 0:
        print('!*50')
        print(Fore.BLUE+Back.WHITE+"PLAYER 1 WINS ")
        print('!'*50)

        break
    elif len(player2.hand.created_cards) == 0: 
         print('!*50')
         print(Fore.BLUE+Back.WHITE+"PLAYER 2 WINS ")
         print('!*50')
         break
    elif count == 12:
        player1.hand.shuffle()
        player2.hand.shuffle()
        count = 0
        
    
print(Fore.WHITE+Back.RED+'GAME OVER')
print('~-_'*50)
print(Style.RESET_ALL)
        
        
        
        
    
            
                    
            



