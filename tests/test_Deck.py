import pytest

from Cardlib import Deck, Hand
from Gamelib import Player


def test_deck_size_of_52():
    """check Deck size to be 52 cards"""
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck_shuffle():
    """check if deck is shuffled"""
    deck1 = Deck()
    deck1.shuffle()
    deck2 = Deck()
    deck2.shuffle()
    assert deck1 != deck2


def test_deck_setup_hands_makes_empty():
    """Check if all the cards are distributed. By check deck len = 0"""
    deck = Deck()
    players = [Player(name, Hand()) for name in ['player1', 'player2']]
    deck.setup_hands(players)
    assert len(deck.cards) == 0


def test_deck_setup_hands_for_2_gives_26_each():
    """For 2 player each has 26 cards in their hand"""
    deck = Deck()
    player1 = Player('player1', Hand())
    player2 = Player('player2', Hand())
    players = [player1, player2]
    deck.setup_hands(players)
    assert len(player1.hand.cards) == 26
    assert len(player2.hand.cards) == 26


def test_deck_setup_hands_for_4_gives_13_each():
    """For 4 player each has 13 cards in their hand"""
    deck = Deck()
    player1 = Player('player1', Hand())
    player2 = Player('player2', Hand())
    player3 = Player('player3', Hand())
    player4 = Player('player4', Hand())
    players = [player1, player2, player3, player4]
    deck.setup_hands(players)
    assert len(player1.hand.cards) == 13
    assert len(player2.hand.cards) == 13
    assert len(player3.hand.cards) == 13
    assert len(player4.hand.cards) == 13
