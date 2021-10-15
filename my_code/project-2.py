'''
Black Jack
'''
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


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
        self.deck = []

        for suit in suits:
            for rank in ranks:
                # Create card objects
                created_card = Card(suit, rank)
                # Add card to all_cards
                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        if self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips: Chips):
    while True:
        try:
            bet = int(input('How many chips you like to bet? '))
        except ValueError:
            print('Sorry, a be must be an integer!')
        else:

            if bet <= chips.total:
                chips.bet += bet
                chips.total -= bet
                break
            else:
                print(
                    f'You do not have enough chips to place this bid! You have {chips.total} chips')


def hit(deck: Deck, hand: Hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: Deck, hand: Hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s\n')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands Dealer\'s turn.')
            playing = False
        else:
            print('You did not enter h or s. Please try again')
            continue

        break


def show_some(player: Hand, dealer: Hand):

    # Show one card from dealers cards
    print('\nDealerr\'s Hand:')
    print('First card is hidden!')
    print(dealer.cards[1])

    # Show player all cards
    print('\nPlayer\'sHand:')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    # Show all dealers cards
    print('\nDealer\'s h Hand:')
    for card in player.cards:
        print(card)

    # Calculate and display value
    print(f'Value of Dealer\'s hand is: {dealer.value}')

    # Show players all cards
    print('\nPlayer\'s Hand:')
    for card in player.cards:
        print(card)

    # Calculate value
    print(f'Value of Player\'s hand is: {player.value}')


def player_busts(player: Hand, dealer: Hand, chips: Chips):
    print('PLAYER BUST!')
    chips.lose_bet()


def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print('DEALER BUST!')
    chips.win_bet()


def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print('DEALER WIN')
    chips.lose_bet()


def push(player: Hand, dealer: Hand, chips: Chips):
    print('Dealer and Player tie! PUSH')


# start the game
playing = True

while True:
    # Print an opening statement
    print('Welcome to BlackJack')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value < 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\nPlayer total chips are at: {player_chips.total}")
    # Ask to play again
    new_game = input('Would you like to play another hand? y/n\n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing BlackJack")
        break
