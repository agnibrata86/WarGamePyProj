import pytest

from Cardlib import Card

"""
Its always card's actual value - 2.
Actual values of cards with face values are : [J - 11, Q - 12,  K - 13, A - 14]
"""


def test_card_invalid_rank():
    with pytest.raises(AssertionError):
        card = Card('H', '13')


def test_card_invalid_suit():
    with pytest.raises(AssertionError):
        card = Card('E', '3')


def test_card_value_of_5():
    card = Card('H', '5')
    card_value = card.value + 2
    assert card_value == 5


def test_card_value_of_10():
    card = Card('D', '10')
    card_value = card.value + 2
    assert card_value == 10


def test_card_value_of_jack():
    card = Card('S', 'J')
    card_value = card.value + 2
    assert card_value == 11


def test_card_value_of_king():
    card = Card('C', 'K')
    card_value = card.value + 2
    assert card_value == 13


def test_card_value_of_ace():
    card = Card('C', 'A')
    card_value = card.value + 2
    assert card_value == 14


def test_card_validity():
    card = Card('H', '3')
    assert card.value == 1
