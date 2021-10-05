from os import system, name
from random import randint


def clear_output():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def tick_tack_toe():

    # function to display board
    def display_board(board):
        clear_output()
        print('     |     |')
        print("  " + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
        print('     |     |')
        print('-'*17)
        print('     |     |')
        print("  " + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
        print('     |     |')
        print('-'*17)
        print('     |     |')
        print("  " + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
        print('     |     |')

    # function to assign user to 'X' or 'O'
    def player_input():
        '''
        OUTPUT = (Player 1 marker, Player 2 marker)
        '''
        choice = None

        while choice not in ['X', 'O']:
            choice = input("Player 1 do you want to be 'X' or 'O': ")

            # if choice is not 'X' or 'O' print message saying wring input
            if choice not in ['X', 'O']:
                print("Invalid input! Please enter 'X' or 'O'")

        if choice == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    # function to place marker at position
    def place_marker(board, marker, position):
        board[position] = marker

    # check if there is winner
    def win_check(board, mark):

        return (board[1] == board[2] == board[3] == mark or
                board[1] == board[5] == board[9] == mark or
                board[1] == board[4] == board[7] == mark or
                board[2] == board[5] == board[8] == mark or
                board[3] == board[6] == board[9] == mark or
                board[4] == board[5] == board[6] == mark or
                board[7] == board[8] == board[9] == mark or
                board[7] == board[5] == board[3] == mark
                )

    # randomly decide who goes first
    def choose_first():
        turn = randint(1, 2)
        if turn == 1:
            print("Player 1 goes first")
            return 'Player 1'
        else:
            print("Player 2 goes first")
            return 'Player 2'

    # check if space is avaliable on board
    def space_check(board, position):
        return board[position] == ' '

    # check if board is full
    def full_board_check(board):
        return not ' ' in board

    # get user input for position
    def player_choice(board):
        player_position_choice = None
        acceptable_range = range(1, 10)

        while True:
            player_position_choice = int(
                input('Please enter position you want to play. 1 to 9: '))
            if player_position_choice in acceptable_range:
                if space_check(board, player_position_choice):
                    return player_position_choice
                else:
                    print('This position is already taken choose another')
            else:
                print('Out of range. Please enter number 1 trough 9.')

    def replay():
        choice = None

        while choice not in ['Y', 'N']:
            choice = input('Keep playing? (Y or N): ')

            if choice not in ['Y', 'N']:
                print('Do not know what it means, please enter Y or N')

        if choice == 'Y':
            return True
        else:
            return False

    # start game
    clear_output()
    print('Welcome to Tic Tac Toe!')
    print()

    while True:
        # Set up game
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')

        game_on = True

        # Play the game
        while game_on:

            if turn == 'Player 1':
                # Show the board
                display_board(board)

                # choose position
                position = player_choice(board)

                # place marker
                place_marker(board, player1_marker, position)

                # check if won
                is_win = win_check(board, player1_marker)

                # check if tie
                is_tie = full_board_check(board)
                # no win or tie? next players turn

                if is_win:
                    display_board(board)
                    print(turn + ' won')
                    game_on = False
                elif is_tie:
                    display_board(board)
                    print('No moves. Game ties.')
                    game_on = False
                else:
                    turn = "Player 2"
            else:
                # Show the board
                display_board(board)

                # choose position
                position = player_choice(board)

                # place marker
                place_marker(board, player2_marker, position)

                # check if won
                is_win = win_check(board, player2_marker)

                # check if tie
                is_tie = full_board_check(board)
                # no win or tie? next players turn

                if is_win:
                    display_board(board)
                    print(turn + ' won')
                    game_on = False
                elif is_tie:
                    display_board(board)
                    print('No moves. Game ties.')
                    game_on = False
                else:
                    turn = "Player 1"

        want_to_play = replay()
        if not want_to_play:
            break


tick_tack_toe()

# from IPython.display import clear_output


# def display_board(board):
#     print("Here is the current list: ")
#     print(board)


# def user_input():

#     # Variables

#     # Initial
#     choice = 'WRONG'
#     acceptable_range = range(0, 10)
#     within_the_range = False

#     # In while loop we need to check two conditions
#     # isdigit and whithin_the_range

#     while choice.isdigit() == False or within_the_range == False:

#         choice = input("Please enter a number (0-10): ")

#         # Digit check
#         if choice.isdigit() == False:
#             print("Sorry, that is not a digit!")

#         # Range check
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_the_range = True
#             else:
#                 print("Sorry, out of the range (0-10)")
#                 within_the_range = False

#     return int(choice)


# def position_choice():

#     choice = None

#     while choice not in ['1', '2', '0']:
#         choice = input('Please enter position 0, 1 or 2: ')

#         if choice not in ['1', '2', '0']:
#             print('Sorry, invalid input, please enter 0, 1 or 2')

#     return int(choice)


# def gameon_choice():
#     choice = None

#     while choice not in ['Y', 'N']:
#         choice = input('Keep playing? (Y or N): ')

#         if choice not in ['Y', 'N']:
#             print('Sorry, invalid input, please enter Y or N')

#     if choice == 'Y':
#         return True
#     else:
#         return False


# def replacement_choice(board, position):

#     user_placement = input("Type a string to place at the position: ")

#     board[position] = user_placement

#     return board


# board = [0, 1, 2]
# game_on = True

# while game_on:
#     display_board(board)

#     position = position_choice()

#     board = replacement_choice(board, position)

#     display_board(board)

#     gameon_choice()
