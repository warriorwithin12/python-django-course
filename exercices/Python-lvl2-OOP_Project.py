#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'HEARTS DIAMONDS SPADES CLUBS'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Card:    
    """
    This is the Card class to represents a single card.
    A card have one value and suite (aka: hearts, clubs, diamonds and spades).
    """    
    def __init__(self, value, suite):
        """
        Initialize one card by it's value and suite type.
        """
        self.value = value
        self.suite = suite

    def __str__(self):
        """
        Returns a strings representing one single card.
        """
        return "Card: {}, {}".format(self.value, self.suite)

    def __cmp__(self, other):
        """
        Compares two card by value and suite type.
        """
        if self.value == other.value and self.suite == other.suite:
            return 0
        elif self.value > other.value:
            return 1
        else:
            return -1

    def __eq__(self, value):
        """
        Check if two cards are the same.
        """
        return self.value == value.value and self.suite == value.suite


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        """
        Generates a new deck with a set of 52 randomized cards.
        """
        self.cards = []
        for card in range(52):
            card = self.pick_card()            
            while (card in self.cards):
                card = self.pick_card()
            self.cards.append(card)

    def pick_card(self):
        """
        Pick one random card.
        """
        shuffle(RANKS)
        shuffle(SUITE)
        return Card(RANKS[0], SUITE[0])

    def split_deck(self):
        """
        Split the deck in two halfs parts.
        Returns tuple with two halfs parts.
        """
        return (self.cards[:int(len(self.cards)/2)], self.cards[int(len(self.cards)/2):])


    def __str__(self):
        # return "Deck: {}".format(super().__str__(self))
        return "Deck: {}".format(self.cards)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        if card not in self.cards:
            self.cards.append(card)

    def __delattr__(self, name):
        return super().__delattr__(name)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
d = Deck()
# for c in d.cards:
#     print(c)
splitted_deck = d.split_deck()
print("First half:", len(splitted_deck[0]))
print("Last half:", len(splitted_deck[1]))