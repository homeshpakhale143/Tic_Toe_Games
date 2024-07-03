

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if there is a winner
def is_winner(player):
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    current_player = 'X'
    while True:
        print("Player " + current_player + "'s turn.")
        position = int(input("Enter a position (1-9): ")) - 1
        if position < 0 or position > 8:
            print("Invalid position. Please try again.")
            continue
        if board[position] != ' ':
            print("Position already taken. Please try again.")
            continue
        make_move(current_player, position)
        print_board()
        if is_winner(current_player):
            print("Player " + current_player + " wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
