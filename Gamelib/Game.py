from Gamelib import Player
from Cardlib import Hand
from Cardlib import Deck
from Gamelib import Pool


class Game:
    """
    Game class for 2 Players. It has methods as below:
        deal_cards
        play_once
        count_round
        play_all
        show_winner
        finished - is property True or False
    """

    def __init__(self, players):
        """
        Initialize the game with Players as input.
        @param players: A list of 2 players.
        """
        self.players = [Player(name, Hand()) for name in players]
        self.deck = Deck()
        self.rounds = 0

    def deal_cards(self):
        """
        Distribute cards to both the players.
        """
        self.deck.shuffle()
        self.deck.setup_hands(self.players)
        for player in self.players:
            print(str(player))

    def play_once(self, tied=False):
        """
        Called in every round of the game. Its recursively called until there is a winner.
        @param tied: Checks if the round is tied or not. The value can be None or Player
        @return: returns the winner.
        """
        if tied is False:
            self.count_round()
        else:
            print('..Its a Tie..')
        pool = Pool()

        for player in self.players:
            if tied:
                player.drop_bonus(pool, 3)
            player.drop_card(pool)
        winner = pool.winner
        if winner is not None:
            pool.reward(winner)
            print('**** Round winner is {} ****'.format(winner.name))
        else:
            winner = self.play_once(pool.tied)
            pool.reward(winner)

        return winner

    def count_round(self):
        """
        This function keep track of rounds.
        """
        self.rounds += 1
        st = 'Starting round {}'.format(self.rounds)
        ln = '================'
        print('\n{}\n{}'.format(st, ln))

    def play_all(self):
        """
        Starting of the game. Called until finished and show the winner.
        """
        while not self.finished:
            self.play_once()
        self.show_winner()

    def show_winner(self):
        """
        Prints the winner who has cards only.
        """
        for player in self.players:
            if player.hand.has_cards:
                print()
                print(player.name, 'wins the WAR!!')
                break

    @property
    def finished(self):
        """
        Checks if only player has the Cards.
        @return: True or False
        """
        return sum(bool(player.hand.cards) for player in self.players) == 1
