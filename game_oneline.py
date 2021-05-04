

def display(gamelist):
    print("current gamelist is  : {}".format(gamelist))
    

def user_input():
    
    while True:
        pos = input("enter the position to insert : (0 ,1, 2) ")
        if pos.isdigit():
            if pos in ['0','1','2']:
                break
            else:
                print("value out of range ")
        else:
            print("invalid input")
    return int(pos)
                
def new_val(gamelist,pos):
    new_val = input("enter the string to be inserted : ")
    
    gamelist[pos]= new_val
    
    
    return gamelist
def game_on():
    while True:
        choice = input("do you want to play on :(y/n) : ")
        if choice in ['y','n','Y','N']:
            break
        else:
            print("sorry, invalid entry ")
    return choice == 'Y' or choice=='y'

def game():
    gamelist = [0,1,2]
    display(gamelist)
    new_gamelist = gamelist
    while True:
        
        pos = user_input()
        new_gamelist = new_val(new_gamelist,pos)
        display(new_gamelist)
        if not game_on():
            break
        else:
            pass
game()
            