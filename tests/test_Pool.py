import pytest

from Cardlib import Hand, Card
from Gamelib import Player, Pool


@pytest.fixture
def pool_with_diff_value_card():
    """setting pool with different value cards."""
    card1, card2 = Card('D', '5'), Card('S', '8')
    player1, player2 = Player('Player1', Hand()), Player('Player2', Hand())
    player1.hand.add_card(card1)
    player2.hand.add_card(card2)
    pool = Pool()
    pool.add_card(player1.hand.take_top(), player1)
    pool.add_card(player2.hand.take_top(), player2)
    return pool


@pytest.fixture
def pool_with_same_value_card():
    """setting pool with some same value cards."""
    player1, player2 = Player('Player1', Hand()), Player('Player2', Hand())
    player1.hand.cards = [Card('D', 'A'), Card('D', '8'), Card('H', '3'), Card('S', '9'), Card('C', 'Q')]
    player2.hand.cards = [Card('H', 'A'), Card('C', 'J'), Card('H', '2'), Card('S', '2'), Card('S', 'A')]
    pool = Pool()
    pool.add_card(player1.hand.take_top(), player1)
    pool.add_card(player2.hand.take_top(), player2)
    pool.add_bonus([player1.hand.take_top(), player1.hand.take_top(), player1.hand.take_top(),
                    player2.hand.take_top(), player2.hand.take_top(), player2.hand.take_top()])
    pool.add_card(player1.hand.take_top(), player1)
    pool.add_card(player2.hand.take_top(), player2)

    return pool


def test_pool_empty_initialization():
    """Empty pool initialization"""
    pool = Pool()
    assert len(pool.cards) == 0
    assert len(pool.players) == 0
    assert len(pool.bonus) == 0


def test_pool_add_card_1():
    """Adding 1 card to pool"""
    player1 = Player('Player1', Hand())
    card1 = Card('D', 'A')
    pool = Pool()
    pool.add_card(card1, player1)
    assert str(pool) == '[D-A :: Player1]'


def test_pool_add_card_multiple():
    """ Adding multiple cards to pool using add_card """
    player1 = Player('Player1', Hand())
    card1 = Card('D', 'A')
    player2 = Player('Player2', Hand())
    card2 = Card('C', '5')
    player3 = Player('Player3', Hand())
    card3 = Card('S', '10')
    pool = Pool()
    pool.add_card(card1, player1)
    pool.add_card(card2, player2)
    pool.add_card(card3, player3)
    assert str(pool) == '[D-A :: Player1, C-5 :: Player2, S-10 :: Player3]'


def test_pool_add_bonus_when_tie():
    """Adding cards to bonus bucket of pool."""
    player1 = Player('Player1', Hand())
    card1 = Card('D', '5')
    player2 = Player('Player2', Hand())
    card2 = Card('C', '5')
    pool = Pool()
    pool.add_card(card1, player1)
    pool.add_card(card2, player2)
    cards = [Card('H', '6'), Card('S', '8'), Card('D', '6')]
    pool.add_bonus(cards)
    assert len(pool.bonus) == len(cards)


def test_pool_winner_cards_value_differ():
    """Pool winner when card value differ"""
    player1 = Player('Player1', Hand())
    card1 = Card('D', '5')
    player2 = Player('Player2', Hand())
    card2 = Card('S', '8')
    pool = Pool()
    pool.add_card(card1, player1)
    pool.add_card(card2, player2)
    assert pool.winner.name == 'Player2'


def test_pool_winner_cards_value_same():
    """Pool winner is None when card value same"""
    player1 = Player('Player1', Hand())
    card1 = Card('D', '5')
    player2 = Player('Player2', Hand())
    card2 = Card('S', '5')
    pool = Pool()
    pool.add_card(card1, player1)
    pool.add_card(card2, player2)
    assert pool.winner is None


def test_pool_reward_with_no_tie(pool_with_diff_value_card):
    """Reward cards to pool winner, with out tie"""
    pool = pool_with_diff_value_card
    player2 = pool_with_diff_value_card.players[1]
    player1 = pool_with_diff_value_card.players[0]
    pool.reward(player2)
    assert len(player2.hand.cards) == 2
    assert len(player1.hand.cards) == 0


def test_pool_reward_with_tie(pool_with_same_value_card):
    """Reward cards to pool winner, with tie"""
    pool = pool_with_same_value_card
    player2 = pool_with_same_value_card.players[1]
    player1 = pool_with_same_value_card.players[0]
    pool.reward(player2)
    assert len(player2.hand.cards) == 10
    assert len(player1.hand.cards) == 0


def test_pool_tied():
    """Pool is tied"""
    pool = Pool()
    assert pool.tied
