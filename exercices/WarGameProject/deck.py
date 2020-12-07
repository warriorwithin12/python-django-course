from random import shuffle

from card import Card
from constants import Constants

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
        shuffle(Constants.RANKS)
        shuffle(Constants.SUITE)
        return Card(Constants.RANKS[0], Constants.SUITE[0])

    def split_deck(self):
        """
        Split the deck in two halfs parts.
        We build the two parts picking one card at a time.
        Returns tuple with two halfs parts.
        """
        half1 = half2 = []
        for i in range(int(len(self.cards)/2)):
            i % 2 == 0 and half1.append(self.cards[i]) or half2.append(self.cards[i+1])
        return half1, half2


    def __str__(self):
        # return "Deck: {}".format(super().__str__(self))
        return "Deck: {}".format(str(self.cards))