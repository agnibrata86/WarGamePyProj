class Player:
    """
    Player class for each player's hand. CURD operation on the Hand of the player.
    """

    def __init__(self, name, hand):
        """
        Initializes the Player with Name and Hand.
        @param name: String for player name.
        @param hand: Hand Object
        """
        self.name, self.hand = name, hand

    def __str__(self):
        """
        Returns the player and hand.
        @return: as PlayerName => Hand
        """
        return '{} => [{}]'.format(self.name, self.hand)

    def drop_card(self, pool):
        """
        At the start of a round Player drops the top card.
        @param pool: Pool object for a round
        """
        if self.hand.has_cards:
            top_card = self.hand.take_top()
            pool.add_card(top_card, self)
            self.laid_cards('Single', top_card)

    def drop_bonus(self, pool, count):
        """
        Player drops the 3 bonus card to the pool when there is tie.
        @param pool: Pool object for that round.
        @param count: Number of cards to be dropped to the pool for the tie. i.e 3
        """
        bonus_cards = self.hand.cards[:count]
        pool.add_bonus(bonus_cards)
        self.hand.cards = self.hand.cards[count:]
        self.laid_cards('WAR', [card.__str__() for card in bonus_cards])

    def give_cards(self, cards):
        """
        Player gets or add cards to the Hand after the win of the round.
        @param cards: List of Cards Object.
        """
        self.hand.add_all(cards)

    def laid_cards(self, card_type, cards):
        """
        Prints the laid single card or bonus(WAR) cards of the player.
        @param card_type: string 'Single' or 'WAR'
        @param cards: card or list of bonus cards
        """
        print('{} laid {} card(s) => {}'.format(self.name, card_type, cards))

