
def display_board(board):
    print("Here is the current list: ")
    print(board)


def user_input():

    # Variables

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0, 10)
    within_the_range = False

    # In while loop we need to check two conditions
    # isdigit and whithin_the_range

    while choice.isdigit() == False or within_the_range == False:

        choice = input("Please enter a number (0-10): ")

        # Digit check
        if choice.isdigit() == False:
            print("Sorry, that is not a digit!")

        # Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_the_range = True
            else:
                print("Sorry, out of the range (0-10)")
                within_the_range = False

    return int(choice)

def position_choice():

    choice = None

    while choice not in ['1', '2', '0']:
        choice = input('Please enter position 0, 1 or 2: ')

        if choice not in ['1', '2', '0']:
            print('Sorry, invalid input, please enter 0, 1 or 2')

    return int(choice)

def gameon_choice():
    choice = None

    while choice not in ['Y', 'N']:
        choice = input('Keep playing? (Y or N): ')

        if choice not in ['Y', 'N']:
            print('Sorry, invalid input, please enter Y or N')

    if choice == 'Y':
        return True
    else:
        return False

def replacement_choice(board,position):
    
    user_placement = input("Type a string to place at the position: ")
    
    board[position] = user_placement
    
    return board

board = [0, 1, 2]
game_on = True

while game_on:
    display_board(board)

    position = position_choice()

    board = replacement_choice(board, position)
    
    display_board(board)

    gameon_choice()
