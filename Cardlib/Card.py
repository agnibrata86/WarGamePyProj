class Card:
    """
    Card class for card with suite and rank.
    """
    SUITES = ['H', 'D', 'S', 'C']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suite, rank):
        """
        Initialize with suite and rank.
        @param suite: Are of Diamond - D, Heart - H, Spade - S, Club - C
        @param rank: Are '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J' - Jack , 'Q' - Queen, 'K' - King, 'A' - Ace
        """
        assert rank in Card.RANKS
        assert suite in Card.SUITES
        self.suite, self.rank = suite, rank

    def __str__(self):
        """
        Returns the suite and rank of a card.
        @return: as suite-rank
        """
        return '{}-{}'.format(self.suite, self.rank)

    @property
    def value(self):
        """
        Returns the value of a card based on index in Rank list.
        @return: Number (its always card actual value - 2).
        Actual values of cards with face values are : [J - 11, Q - 12,  K - 13, A - 14]
        """
        return self.RANKS.index(self.rank)
