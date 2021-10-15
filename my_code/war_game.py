'''
War Game
'''
from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# Create Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


# Create Deck Class
class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card objects
                created_card = Card(suit, rank)
                # Add card to all_cards
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Create Player Class
class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # if we have multiple cards
            self.all_cards.extend(new_cards)
        else:
            # when we have single card
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME LOGIC

# Game Setup
# Create two players
num_cards_to_draw = 5
player1 = Player('One')
player2 = Player('Two')

# Create a deck
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Split the deck between players
for i in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())

print(player1)
print(player2)


# Start the game
game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    # Check if any player is lost
    # Player One
    if len(player1.all_cards) == 0:
        print('Player One out of cards.\nPlayer Two WINS!')
        game_on = False
        break

    # Player Two
    if len(player2.all_cards) == 0:
        print('Player Two out of cards.\nPlayer One WINS!')
        game_on = False
        break

    # Start new round
    player1_cards = []

    player2_cards = []

    player1_cards.append(player1.remove_one())
    player2_cards.append(player2.remove_one())

    at_war = True

    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:

            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)

            at_war = False

        elif player1_cards[-1].value < player2_cards[-1].value:

            player2.add_cards(player2_cards)
            player2.add_cards(player1_cards)

            at_war = False

        else:
            print("WAR!")

            if len(player1.all_cards) < num_cards_to_draw:
                print('Player One unable to declare war')
                print("Player Two WINS")
                game_on = False
                break

            elif len(player2.all_cards) < num_cards_to_draw:
                print('Player Two unable to declare war')
                print("Player One WINS")
                game_on = False
                break

            else:
                for num in range(num_cards_to_draw):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
