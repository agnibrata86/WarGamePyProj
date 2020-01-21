import pytest

from Cardlib import Card

"""
Its always card's actual value - 2.
Actual values of cards with face values are : [J - 11, Q - 12,  K - 13, A - 14]
"""


def test_card_invalid_rank():
    """create a card with invalid Rank"""
    with pytest.raises(AssertionError):
        card = Card('H', '13')


def test_card_invalid_suite():
    """create a card with invalid suite"""
    with pytest.raises(AssertionError):
        card = Card('E', '3')


def test_card_value_of_5():
    """create a card with value = 5"""
    card = Card('H', '5')
    card_value = card.value + 2
    assert card_value == 5


def test_card_value_of_10():
    """create a card with value = 10"""
    card = Card('D', '10')
    card_value = card.value + 2
    assert card_value == 10


def test_card_value_of_jack():
    """create a card with face value = J"""
    card = Card('S', 'J')
    card_value = card.value + 2
    assert card_value == 11


def test_card_value_of_king():
    """create a card with face value = K"""
    card = Card('C', 'K')
    card_value = card.value + 2
    assert card_value == 13


def test_card_value_of_ace():
    """create a card with face value = A"""
    card = Card('C', 'A')
    card_value = card.value + 2
    assert card_value == 14


def test_card_validity():
    """Check card value is card.value - 2  as its returned as Index in Card.RANK"""
    card = Card('H', '3')
    assert card.value == 1
