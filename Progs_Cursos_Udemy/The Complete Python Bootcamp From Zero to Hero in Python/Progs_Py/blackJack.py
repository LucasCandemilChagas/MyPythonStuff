import random

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 
              'Queen': 10, 'King': 10, 'Ace': 11}
game_on = True

player_total = 100
player_bet = 0
player_winnings = 0

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
        self.value = 0
        self.aces = 0
    
    def remove_one(self):
        return self.hand.pop(0)      
       
    #Add one card to the player hand  
    def add_card(self,new_card):
        self.hand.append(new_card)
        self.value += values[new_card.rank]
        
        if new_card.rank == 'Ace':
            self.aces += 1
     
    def adjust_for_ace(self):
        
        #if total value > 21 and i still have ace cards
        # than change my ace value to 1 instead of 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
     
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards with {self.value} value'

def win_bet():
    global player_total
    player_total += player_bet

def lose_bet():
    global player_total
    player_total -= player_bet

def reset():
    dealer = Player('Dealer')
    deck = Deck()
    deck.shuffle()
    p1 = Player('Lucas')
    for i in range(2):
        p1.add_card(deck.grab_card())
        dealer.add_card(deck.grab_card())
    
def check_win():
    if p1.value < dealer.value and dealer.value < 21:
        print(f'You Lose! - Dealer hand value: {dealer.value} and Player hand value: {p1.value}')
        lose_bet()
        print("\nPlayer's winnings stand at", player_total)
        game_on = False
    else:
        print('You Win!')
        win_bet()
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at", player_total)
        game_on = False

dealer = Player('Dealer')

deck = Deck()

deck.shuffle()

player_bet = int(input('Insert your bet: '))

while player_bet > player_total:
    player_bet = int(input(f'Error, bet is higher than your chips ({player_total}), please try again: '))    
    
p1 = Player('Lucas')
while game_on:
    for i in range(2):
        p1.add_card(deck.grab_card())
        dealer.add_card(deck.grab_card())
        
    print(f'Dealer has {dealer.hand[0]} - Value: {dealer.value}')
    print(f'Player has {p1.hand[0]} and {p1.hand[1]}')

    hit = input('Do you wanna hit? (y/n): ').capitalize()
    
    while hit == 'Y':
        print('Player Hit!')
        p1.add_card(deck.grab_card())
        p1.adjust_for_ace()
        hit = input('Do you wanna hit? (y/n): ').capitalize()
        
    
    if p1.value <= 21: 
        print('Dealer is playing!')	   
        while dealer.value < 17:
            print('Dealer Hit!')
            dealer.add_card(deck.grab_card())
            dealer.adjust_for_ace()
            
    check_win()
 
    gameon = input('Wanna play again? (y/n): ').capitalize()
    
    if gameon == 'Y':
        game_on = True
        reset()
print(p1)