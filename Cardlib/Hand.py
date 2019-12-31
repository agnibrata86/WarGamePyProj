
class Hand:
    """
    Hand class is for players hand with list of cards.
    """

    def __init__(self):
        """
        Initialize the player hand with cards.
        """
        self.cards = []

    def __str__(self):
        """
        This prints player hand with list of cards as string.
        @return: return string of cards
        """
        return ', '.join(map(str, self.cards))

    def add_card(self, card):
        """
        Add card to the hand.
        @param card: takes the card object as input.
        """
        self.cards.append(card)

    def take_top(self):
        """
        Play the top card from the player hand.
        @return:
        """
        return self.cards.pop(0)

    def add_all(self, cards):
        """
        Called after player wins a round, and the cards are added to the bottom.
        @param cards:
        """
        self.cards.extend(cards)

    @property
    def has_cards(self):
        """
        Checks if the player has cards.
        @return: True or False
        """
        return bool(self.cards)