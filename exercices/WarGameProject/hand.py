class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        """
        Add card to hand if not exists previously.
        """
        if card not in self.cards:
            self.cards.append(card)
        else:
            print("Card already in hand! Nothing added.")

    def remove_card(self):
        """
        Remove a card from hand if hand has cards left.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No cards left in hand! Nothing removed.")
            return None

    def __del__(self):
        """
        Delete a hand, deleting it's cards.
        """
        del self.cards
        # print("Deleted cards from Hand")

    def __str__(self):
        return "Hand: {}".format(str(self.cards))

    def len(self):
        return len(self.cards)
