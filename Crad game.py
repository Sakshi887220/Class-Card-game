#For this we need to build for classes
#1 . Card class - Hold the information about the card
#2 . Deck class - Hold the information baout the complete set of 52 cards
#3 . Player class - Hold the information about the cards the player are having
#4 . Table class - Holds the information about the cards on table.

1. This game involves two players and initialy each player is given 26 cards each.
2. They have to put there top card on the table turn wise
3. If the card they are going to put on table matchs with the already top card on the table
MATCH condition - Two cards match if they have same suit OR if they have same rank
4. Player wins that chance and he take all the cards on the table and add all those cards to the end of the deck of cards he
already have.
5. This way game runs until one of the player run out of cards
6. The player that run out of cards losses and other player wins the game!!!!!

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#this class has the information about the a particular card
class Card:

    def __init__(self,suit,rank):
       

        
    def __str__(self):
           #returns a string defining the card



#this class contains the set of 52 cards and each card the obeject of previously defined class card.
class Deck:
    
    def __init__(self):
          # build Card objects and add them to the list
    
    def __str__(self):
        # add each Card object's print string
      

    def shuffle(self):           # Shuffles the 52 cards
               
    def __len__(self):
       

# Player class has all the information about the cards a player is holding
class Player:
    def __init__(self,name):
       
    def add(self , new_cards):          # Add the cards from the table after the persor wins
       
        
    def move(self):                     #Puts one card on the table
      
    def __str__(self):
        
    def __len__(self):
       
   
# this class has the information about all the cards on the table
class Table:
    def __init__(self):
        self.cards = []
    
    def add(self , new_cards):                     #Adds the new card to the table as the player moves 
        self.cards.append(new_cards)
        
    def remove(self):                                #All the cards are removed and given to a particular person
        self.cards = []
    
    def __str__(self):
        ans = ''
        for cards in self.cards:
            ans += '\n' + cards.__str__()
        return "Table has the following cards:" + ans
    def __len__(self):
        return len(self.cards)

# This function takes the input names of the players
def player_name():   
    user_1 = input("Hi! Please enter name of first player")  #stores the name of first user
    print("Hi" , user_1)
    user_2 = input("Hi! Please enter name of second player") #stores the name of second user
    print("Hi" ,user_2)
    return(user_1 ,user_2 )

#Initializing a deck
deck = Deck()
deck.shuffle()
len(deck)

#make new players
name_1 , name_2 = player_name()
user_1 = Player(name_1)
user_2 = Player(name_2)

#Add initial cards
user_1.add(deck.deck[0:26])
user_2.add(deck.deck[26:52])

print(user_1)

print(user_2)

# Intitalizing the new table for our game.
table = Table()

player =1
while(True):
    print("No of cards with",user_1.name,"are",len(user_1))
    print("No of cards with",user_2.name,"are",len(user_2))
    print("No of cards on table are",len(table))
    print('\n')
    if player == 1:
        card = user_1.move()
        print(user_1.name,"Please press enter to move a chance. You have a",card.__str__() ,'\n')
        a = input("Press any key")
        print("Top Cards on table are",'\n')
        

        player = 2
    else :
        card = user_2.move()
        print(user_2.name,"Please press enter to move a chance. You have a",card.__str__(),'\n')
        a = input("Press any key")
        print("Top Cards on table are",'\n')
       


        player = 1
        
    print('\n')
    if len(user_1) == 0:
        print("Congrats",user_2.name,"Won")
        break
    if len(user_2) == 0:
        print("Congrats",user_1.name,"Won")
        break
