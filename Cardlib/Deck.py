import random

from Cardlib import Card


class Deck:
    """
    Deck class is to setup a card game.
    """

    def __init__(self):
        """
        Initializes with 52 cards with suite & rank.
        """
        self.cards = [Card(s, r) for s in Card.SUITES for r in Card.RANKS]

    def __str__(self):
        """
        Returns the suite and rank of all the cards of the Deck.
        @return: as list of SUITE-RANK
        """
        return '[{}]'.format(', '.join(map(str, self.cards)))

    def shuffle(self):
        """
        Random shuffles the deck.
        """
        random.shuffle(self.cards)

    def setup_hands(self, players):
        """
        Setup the hands for each player.
        @param players: is a List of 2 players.
        @return: Returns the list of Hand objects
        """
        hands = [player.hand for player in players]
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands
