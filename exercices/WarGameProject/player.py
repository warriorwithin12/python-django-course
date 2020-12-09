from .hand import Hand

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand: Hand):
        self.name = name
        self.hand = hand

    def play(self, offset):
        played_cards = list(map(lambda c: self.hand.remove_card(), range(offset)))
        return played_cards if len(played_cards) > 0 else None

    def has_cards(self):
        """
        Checks if player has left cards.
        """
        return self.hand.len() > 0

    def __str__(self):
        return self.name

    def __del__(self):
        del self.hand
        print("Deleted player {}".format(self.name))
