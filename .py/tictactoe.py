import random
gameon_choice = True
  
def display_board(game_board):
    print(f' {game_board[7]} | {game_board[8]} | {game_board[9]}')
    print('-----------')
    print(f' {game_board[4]} | {game_board[5]} | {game_board[6]}')
    print('-----------')
    print(f' {game_board[1]} | {game_board[2]} | {game_board[3]}')
    

def game_choice():
    
    choice = 'wrong'
    
    while choice != 'Y' and choice != 'N':
        choice = input('Do you want to continue playing? (Y/N): ').upper()
    if choice == 'Y':
        return True
    if choice == 'N':
        return False

def player_turn(p):
    
    choice = 'Wrong'
    acceptable_range = range(1, 10)
    within_range = False
    
    while not choice.isnumeric() or within_range == False:
        choice = input(f'Player {p} pick a number in range of (1-9): ')
        if choice.isnumeric():
            if int(choice) in acceptable_range and game_board[int(choice)] not in ['X', 'O']:
                within_range = True
                           
    game_board[int(choice)] = players[p]

def player_XO(players):    
    xO = ' '
    while xO not in ['X', 'O']:
        xO = input('Player 1, choose X or O: ').upper()
        if xO ==  'X' or xO == 'O':
            players[1] = xO
    if players[1] == 'X':
        players[2] = 'O'
    elif players[1] == 'O':
        players[2] = 'X'
        
def verification_win(game_board,p):
    if players[p] == game_board[7] and players[p] == game_board[8] and players[p] == game_board[9]:
        return p
    elif players[p] == game_board[4] and players[p] == game_board[5] and players[p] == game_board[6]:
        return p
    elif players[p] == game_board[1] and players[p] == game_board[2] and players[p] == game_board[3]:
        return p
    elif players[p] == game_board[1] and players[p] == game_board[4] and players[p] == game_board[7]:
        return p
    elif players[p] == game_board[2] and players[p] == game_board[5] and players[p] == game_board[8]:
        return p
    elif players[p] == game_board[3] and players[p] == game_board[6] and players[p] == game_board[9]:
        return p
    elif players[p] == game_board[1] and players[p] == game_board[5] and players[p] == game_board[9]:
        return p
    elif players[p] == game_board[3] and players[p] == game_board[5] and players[p] == game_board[7]:
        return p
    else:
        if not full_board_check(game_board):
            return 3
    
def full_board_check(game_board):
    for i in range(1,10):
        if not (game_board[i] == 'X' or game_board[i] == 'O'):
            return True
    return False    

  
while gameon_choice:
    #reset
    game_board = [' ']*10
    players = [' ']*3
    game_win = 0
    
    #chose what player will get X/O
    player_XO(players)
    
    #randomize what player will go first
    p = random.randint(1,2)
    
    #verifies if player 1 or 2 wins or if it is a tie
    while game_win not in [1,2,3]:
        
        print('\n'*100)
        
        display_board(game_board)
        
        if full_board_check(game_board):
            player_turn(p)
            
        #check every turn if player won 
        game_win = verification_win(game_board, p)
        
        if p == 1:
            p = 2
        else:
            p = 1
    print('\n'*100)
    display_board(game_board)
    if game_win < 3:        
        print(f'Player {game_win} is the winner!')
    else:
        print('It is a TIE!')
    gameon_choice = game_choice()