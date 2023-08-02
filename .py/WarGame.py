import random
suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 
              'Queen': 12, 'King': 13, 'Ace': 14}
game_on = True

class Card:

    def __init__(self, suit, rank):      
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    all_cards = []
    
    def __init__(self):
    
        for suit in suits:
            for rank in ranks:
                #Create an Card object
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def grab_card(self):
        return self.all_cards[random.randint(0, 51)]    
    
class Player:
 
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def remove_one(self):
        return self.hand.pop(0)
    
    #Add one Card object in his hand  
    def add_one(self, new_card):
        self.hand.append(new_card)
        
    #Add multiple Card objects in his hand    
    def add_cards(self,new_cards):
        if(type(new_cards) == type([])):
            self.hand.extend(new_cards)
     
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'
    
deck = Deck()

#Shuffle cards in the deck
deck.shuffle()

ply1 = Player('Lucas')
ply2 = Player('Gauterio')

for i in range(26):
    ply1.add_one(deck.grab_card())
    ply2.add_one(deck.grab_card())

#Game Logic
#while that if game is still in progress it stays inside the while
round_num = 0

while game_on:
    
    round_num += 1
    print(f'Round {round_num}')
    if len(ply1.hand) < 5 or len(ply2.hand) < 5:
        game_on = False
        break
    
    player_one_cards = [] #cards on the table
    player_one_cards.append(ply1.remove_one())
    player_two_cards = [] #cards on the table
    player_two_cards.append(ply2.remove_one())
    
    at_war = True
    
    while at_war:
        #if-elif-else that see if the value of the card picked is 
        # higher than the other player and if they are equal it continues inside this while
        if player_one_cards[-1].value > player_two_cards[-1].value:
            #Player 1 picks the cards from the table 
            ply1.add_cards(player_one_cards)
            ply1.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            #Player 2 picks the cards from the table 
            ply2.add_cards(player_one_cards)
            ply2.add_cards(player_two_cards)
            at_war = False
        else:
            print('\n')
            print('At War\n')
            print(f'Player 1 num of cards: {len(ply1.hand)} cards')
            print(f'Player 2 num of cards: {len(ply2.hand)} cards\n')
            if len(ply1.hand) < 5 or len(ply2.hand) < 5:
                at_war = False
                game_on = False
                break
            for i in range(5):
                player_one_cards.append(ply1.remove_one())
                player_two_cards.append(ply2.remove_one())
            print(f'Player 1 ends with: {len(ply1.hand)} cards')
            print(f'Player 2 ends with: {len(ply2.hand)} cards\n')         
if len(ply1.hand) > len(ply2.hand):
    print('Player 1 has Won!!!')
else:
    print('Player 2 has Won!!!')