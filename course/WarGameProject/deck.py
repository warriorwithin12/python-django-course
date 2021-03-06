from random import shuffle

from .card import Card
from .constants import Constants

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
            while card in self.cards:
                card = self.pick_card()
            self.cards.append(card)

    def pick_card(self):
        """
        Pick one random card.
        """
        shuffle(Constants.RANKS)
        shuffle(Constants.SUITE)
        return Card(Constants.RANKS[0], Constants.SUITE[0])

    def split_deck(self):
        """
        Split the deck in two halfs parts picking one card at a time.
        """
        return self.cards[0:len(self.cards):2], self.cards[1:len(self.cards):2]

    def __str__(self):
        return "Deck: {}".format(str(self.cards))