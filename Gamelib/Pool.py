class Pool:
    """
    Pool class is created in every round, and it collects the card and corresponding player until the tie is resolved.
    """

    def __init__(self):
        """
        Initialized with empty list of cards, players, bonus (for a tie)
        """
        self.cards = []
        self.players = []
        self.bonus = []
        self.best = None

    def __str__(self):
        """
        Returns the card and corresponding player in the pool.
        @return: print as [CARD :: PlayerName]
        """
        return '[{}]'.format(', '.join(map(lambda x, y: str(x) + ' :: ' + y.name, self.cards, self.players)))

    def add_card(self, card, player):
        """
        Adds card and corresponding player to the pool.
        @param card: Get card object as input.
        @param player: And corresponding player object as input.
        """
        self.cards.append(card)
        self.players.append(player)

    def add_bonus(self, cards):
        """
        Adds the list of cards to bonus when there is a tie.
        @param cards: List of card objects
        """
        self.bonus.extend(cards)

    @property
    def winner(self):
        """
        Checks for the winner by comparing card values of both player.
        Number of Max values =1, then player with max value is winner.
        Returns the player Object that is winner otherwise None.
        @return: Player object or None
        """
        values = [card.value for card in self.cards]
        self.best = max(values)
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def reward(self, player):
        """
        Adds all the cards in the Pool to the winner's hand.
        @param player: winner of the round
        """
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    @property
    def tied(self):
        """
        Returns true as its tie.
        @return: True always
        """
        return True
