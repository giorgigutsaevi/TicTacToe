import random

# Step 1 - Display the board


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Step 2 - function that can take in a player input and assign their marker as 'X' and 'O'.

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

# Step 3 - Write a function that takes in the board list object, and a desired position 1-9 and assigns
# it to the board


def place_marker(board, marker, position):
    board[position] = marker


# Step 4 - takes in a board and a mark as its args, and then checks to see if that mark has won

def win_check(board, mark):
    # What does it mean to win TIC TAC TOE
    # ALL ROWS, COLUMNS and DIAGONALS Check all rows and check if they share the same marker?
    return (board[1] == board[2] == board[3] == mark) or \
           (board[4] == board[5] == board[6] == mark) or \
           (board[7] == board[8] == board[9] == mark) or \
           (board[7] == board[4] == board[1] == mark) or \
           (board[8] == board[5] == board[2] == mark) or \
           (board[9] == board[6] == board[3] == mark) or \
           (board[7] == board[5] == board[3] == mark) or \
           (board[9] == board[5] == board[1] == mark)


# Step 5 - function that returns a bool and randomly decides which player goes first

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Step 6 - function that returns a bool indicating whether a space on the board is available

def space_check(board, position):
    return board[position] == ' '


# Step 7 - function that checks if the board is full and returns a bool. True if full, false otherwise

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if we return True
    return True

# Step 8 - Function that asks for a player's next position (number 1-9).
# Then it uses the function from step 6 to check if it's a free position.


def player_choice(board):

    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
    return position


# Step 9 - Asks the player if the player wants to go again

def replay():
    choice = input("Do you want to play again? Enter Yes or No: ")
    return choice == "Yes"


# Step 10 - The logic/flow part

# While loop to keep running the game
print('Welcome to Tic Tac Toe Game!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
