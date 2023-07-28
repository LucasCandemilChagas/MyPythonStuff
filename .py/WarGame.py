import random
suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 
              'Queen': 12, 'King': 13, 'Ace': 14}
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
    def add_one(self, new_cards):
        self.hand.append(new_cards.pop(0))
        
    #Add multiple Card objects in his hand    
    def add_mult(self, num, new_cards):
        for i in range(0, num):
            self.hand.append(new_cards.pop(0))
     
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'     
             
new_deck = Deck()
new_deck.shuffle()
bottom_card = new_deck.all_cards[-1]
player1 = Player('Lucas')

player1.add_one(new_deck.all_cards)
player1.add_mult(4, new_deck.all_cards)

print(player1)


