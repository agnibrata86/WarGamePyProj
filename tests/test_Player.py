import pytest

from Cardlib import Hand, Card
from Gamelib import Player, Pool


@pytest.fixture
def players():
    player1, player2 = Player('Player1', Hand()), Player('Player2', Hand())
    player1.hand.cards = [Card('D', 'A'), Card('D', '8'), Card('H', '3'), Card('S', '9'), Card('C', 'Q')]
    player2.hand.cards = [Card('H', 'A'), Card('C', 'J'), Card('H', '2'), Card('S', '2'), Card('S', 'A')]
    return [player1, player2]


def test_player_drop_card(players):
    pool = Pool()
    players[0].drop_card(pool)
    players[1].drop_card(pool)
    assert len(players[0].hand.cards) == len(players[1].hand.cards) == 4
    assert len(pool.cards) == 2


def test_player_drop_card_empty_hand():
    player1 = Player('Player1', Hand())
    pool = Pool()
    player1.drop_card(pool)
    assert len(pool.cards) == 0
    assert len(player1.hand.cards) == 0


def test_player_drop_bonus_have_more_than_3_cards(players):
    player1 = players[0]
    pool = Pool()
    player1.drop_bonus(pool, 3)
    assert len(player1.hand.cards) == 2
    assert len(pool.bonus) == 3


def test_player_drop_bonus_have_less_than_3_cards():
    player1 = Player('Player1', Hand())
    player1.hand.cards = [Card('D', 'A'), Card('D', '8')]
    pool = Pool()
    player1.drop_bonus(pool, 3)
    assert len(player1.hand.cards) == 0
    assert len(pool.bonus) == 2


def test_player_give_cards_after_win(players):
    player1 = players[0]
    winning_cards = [Card('H', '7'), Card('S', '6')]
    player1.give_cards(winning_cards)
    assert len(player1.hand.cards) == 7
