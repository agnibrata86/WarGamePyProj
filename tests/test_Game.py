import pytest

from Cardlib import Card, Hand
from Gamelib import Game, Player


@pytest.fixture
def players_cards_with_no_tie():
    """Setting 26 cards to each player with no tie card"""
    player2_cards = [Card('H', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6'),
                     Card('H', '7'), Card('H', '8'), Card('D', '2'), Card('D', '3'), Card('D', '4'),
                     Card('D', '5'), Card('D', '6'), Card('D', '7'), Card('D', '8'), Card('S', '2'),
                     Card('S', '3'), Card('S', '4'), Card('S', '5'), Card('S', '6'), Card('S', '7'),
                     Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6'),
                     Card('C', '7')]
    player1_cards = [Card('H', '9'), Card('H', '10'), Card('H', 'J'), Card('H', 'K'), Card('H', 'Q'),
                     Card('H', 'A'), Card('D', '9'), Card('D', '10'), Card('D', 'J'), Card('D', 'K'),
                     Card('D', 'Q'), Card('D', 'A'), Card('S', '8'), Card('S', '9'), Card('S', '10'),
                     Card('S', 'J'), Card('S', 'K'), Card('S', 'Q'), Card('S', 'A'), Card('C', '8'),
                     Card('C', '9'), Card('C', '10'), Card('C', 'J'), Card('C', 'K'), Card('C', 'Q'),
                     Card('C', 'A')]
    players_cards = [player1_cards, player2_cards]
    return players_cards


@pytest.fixture
def players_cards_with_tie():
    """Setting 26 cards to each player with tie card"""
    player1_cards = [Card('H', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6'),
                     Card('H', '7'), Card('H', '8'), Card('H', '10'), Card('D', '2'), Card('D', '4'),
                     Card('D', '5'), Card('D', '6'), Card('D', '7'), Card('D', '8'), Card('S', '2'),
                     Card('S', '3'), Card('S', '4'), Card('S', '5'), Card('S', '6'), Card('S', '7'),
                     Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6'),
                     Card('C', '7')]
    player2_cards = [Card('H', '9'), Card('D', '3'), Card('H', 'J'), Card('H', 'K'), Card('H', 'Q'),
                     Card('H', 'A'), Card('D', '9'), Card('D', '10'), Card('D', 'J'), Card('D', 'K'),
                     Card('D', 'Q'), Card('D', 'A'), Card('S', '8'), Card('S', '9'), Card('S', '10'),
                     Card('S', 'J'), Card('S', 'K'), Card('S', 'Q'), Card('S', 'A'), Card('C', '8'),
                     Card('C', '9'), Card('C', '10'), Card('C', 'J'), Card('C', 'K'), Card('C', 'Q'),
                     Card('C', 'A')]
    players_cards = [player1_cards, player2_cards]
    return players_cards


@pytest.fixture
def players_having_no_tie_card_sample():
    """Setting 5 sample cards to each player with no tie card"""
    player1_cards = [Card('H', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]
    player2_cards = [Card('H', '9'), Card('H', '10'), Card('H', 'J'), Card('H', 'K'), Card('H', 'Q')]
    return [player1_cards, player2_cards]


@pytest.fixture
def players_having_tie_card_sample():
    """Setting 5 sample cards to each player with tie card"""
    player1_cards = [Card('S', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6'),
                     Card('H', '7')]
    player2_cards = [Card('H', '2'), Card('H', '10'), Card('H', 'J'), Card('H', 'K'), Card('H', 'Q'),
                     Card('H', 'A')]
    return [player1_cards, player2_cards]


def test_game_deal_cards():
    """Distribute all 52 cards to both players, each having a hand of 26 cards."""
    game = Game(['Player1', 'Player2'])
    game.deal_cards()
    assert len(game.players[0].hand.cards) == len(game.players[1].hand.cards) == 26


def test_game_play_once_no_tie(players_having_no_tie_card_sample):
    """Play Once with no tie card, each having 5 cards."""
    players_cards = players_having_no_tie_card_sample
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = players_cards[0]
    game.players[1].hand.cards = players_cards[1]
    winner = game.play_once()
    assert winner.name == 'Player2'


def test_game_play_once_with_tie(players_having_tie_card_sample):
    """Play Once with tie card, each having 5 cards."""
    players_cards = players_having_tie_card_sample
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = players_cards[0]
    game.players[1].hand.cards = players_cards[1]
    winner = game.play_once()
    assert winner.name == 'Player2'


def test_game_play_all_no_tie(players_cards_with_no_tie):
    """Play all with no tie card, each having 26 cards."""
    players_cards = players_cards_with_no_tie
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = players_cards[0]
    game.players[1].hand.cards = players_cards[1]
    winner = game.play_all()
    assert winner == 'Player1'
    assert len(game.players[0].hand.cards) == 52
    assert len(game.players[1].hand.cards) == 0


def test_game_play_all_with_tie(players_cards_with_tie):
    """Play all with tie card, each having 26 cards."""
    players_cards = players_cards_with_tie
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = players_cards[0]
    game.players[1].hand.cards = players_cards[1]
    winner = game.play_all()
    assert winner == 'Player2'
    assert len(game.players[1].hand.cards) == 52
    assert len(game.players[0].hand.cards) == 0


def test_game_finished_no():
    """Finished is False"""
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = [Card('S', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6'),
                                  Card('H', '7')]
    game.players[1].hand.cards = [Card('H', '2'), Card('H', '10'), Card('H', 'J'), Card('H', 'K'), Card('H', 'Q'),
                                  Card('H', 'A')]
    assert not game.finished


def test_game_finished_yes():
    """Finished is True"""
    game = Game(['Player1', 'Player2'])
    game.players[0].hand.cards = [Card('H', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6'),
                                  Card('H', '7'), Card('H', '8'), Card('D', '2'), Card('D', '3'), Card('D', '4'),
                                  Card('D', '5'), Card('D', '6'), Card('D', '7'), Card('D', '8'), Card('S', '2'),
                                  Card('S', '3'), Card('S', '4'), Card('S', '5'), Card('S', '6'), Card('S', '7'),
                                  Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6'),
                                  Card('C', '7'), Card('H', '9'), Card('D', '3'), Card('H', 'J'), Card('H', 'K'),
                                  Card('H', 'Q'), Card('H', 'A'), Card('D', '9'), Card('D', '10'), Card('D', 'J'),
                                  Card('D', 'K'), Card('D', 'Q'), Card('D', 'A'), Card('S', '8'), Card('S', '9'),
                                  Card('S', '10'), Card('S', 'J'), Card('S', 'K'), Card('S', 'Q'), Card('S', 'A'),
                                  Card('C', '8'), Card('C', '9'), Card('C', '10'), Card('C', 'J'), Card('C', 'K'),
                                  Card('C', 'Q'), Card('C', 'A')]
    game.players[1].hand.cards = []
    assert len(game.players[1].hand.cards) == 0
    assert len(game.players[0].hand.cards) == 52
    assert game.finished
