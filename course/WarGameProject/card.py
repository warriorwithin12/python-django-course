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
        return "{}, {}".format(self.value, self.suite)

    def compare(self, other):
        """
        Compares two card by value and suite type.
        """
        return self.value.__cmp__(other.value)

    def __eq__(self, value):
        """
        Check if two cards are the same.
        """
        return self.value == value.value and self.suite == value.suite
