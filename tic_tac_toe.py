import random

# Create the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Define player and bot symbols
player_symbol = 'X'
bot_symbol = 'O'

# Function to display the Tic-Tac-Toe board
def display_board():
    print('-------------')
    for i in range(3):
        print(f'| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |')
        print('-------------')

# Function to check if a player has won
def check_winner(symbol):
    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False

# Function to check if the board is full
def check_board_full():
    return ' ' not in board

# Function to get player's move
def get_player_move():
    while True:
        move = input('Enter your move (1-9): ')
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            return int(move) - 1
        print('Invalid move. Please try again.')

# Function for bot's move
def get_bot_move():
    # Check for possible winning move
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == bot_symbol and board[combo[2]] == ' ':
            return combo[2]
        elif board[combo[0]] == board[combo[2]] == bot_symbol and board[combo[1]] == ' ':
            return combo[1]
        elif board[combo[1]] == board[combo[2]] == bot_symbol and board[combo[0]] == ' ':
            return combo[0]

    # Check for player's possible winning move
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == player_symbol and board[combo[2]] == ' ':
            return combo[2]
        elif board[combo[0]] == board[combo[2]] == player_symbol and board[combo[1]] == ' ':
            return combo[1]
        elif board[combo[1]] == board[combo[2]] == player_symbol and board[combo[0]] == ' ':
            return combo[0]

    # Choose a random move
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(empty_cells)

# Function to start a new game
def start_game():
    global board
    board = [' ' for _ in range(9)]
    display_board()

    while True:
        # Player's turn
        player_move = get_player_move()
        board[player_move] = player_symbol
        display_board()

        if check_winner(player_symbol):
            print('Congratulations! You won!')
            break

        if check_board_full():
            print("It's a tie!")
            break

        # Bot's turn
        print("Bot's turn...")
        bot_move = get_bot_move()
        board[bot_move] = bot_symbol
        display_board()

        if check_winner(bot_symbol):
            print('Oops! Bot won!')
            break

        if check_board_full():
            print("It's a tie!")
            break

# Function to display the main menu
def display_main_menu():
    print('===== Tic-Tac-Toe =====')
    print('1. Start Game')
    print('2. Quit')

# Function to display the end menu
def display_end_menu():
    print('===== Game Over =====')
    print('1. Play Again')
    print('2. Quit')

# Main game loop
while True:
    display_main_menu()
    choice = input('Enter your choice: ')

    if choice == '1':
        start_game()
        display_end_menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            continue
        else:
            break

    elif choice == '2':
        break

    else:
        print('Invalid choice. Please try again.')
