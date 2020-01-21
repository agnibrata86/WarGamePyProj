import pytest

from Cardlib import Hand, Card


def test_hand_empty():
    """ Create empty hand"""
    hand = Hand()
    assert len(hand.cards) == 0


def test_hand_add_card_1():
    """Add 1 card to empty hand."""
    hand = Hand()
    card = Card('D', '5')
    hand.add_card(card)
    assert len(hand.cards) == 1


def test_hand_add_card_multiple():
    """Add multiple cards to empty hand."""
    hand = Hand()
    card = Card('D', '5')
    card1 = Card('C', '10')
    card2 = Card('H', 'A')
    hand.add_card(card)
    hand.add_card(card1)
    hand.add_card(card2)
    assert len(hand.cards) == 3


def test_hand_add_all_to_empty():
    """ Add list of cards to empty Hand"""
    cards = [Card('D', '5'), Card('C', '10'), Card('H', 'A'), Card('S', 'K')]
    hand = Hand()
    hand.add_all(cards)
    assert len(hand.cards) == len(cards)


def test_hand_add_all_to_non_empty():
    """ Add list of cards to non-empty Hand"""
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    hand_cards_len_before_add_all = len(hand.cards)
    assert hand_cards_len_before_add_all == 2
    cards = [Card('D', '5'), Card('C', '10'), Card('H', 'A'), Card('S', 'K')]
    hand.add_all(cards)
    hand_cards_len_after_add_all = len(hand.cards)
    assert hand_cards_len_after_add_all == hand_cards_len_before_add_all + len(cards)


def test_hand_add_all_1_card_as_list():
    """ Add 1 card as list to non-empty Hand"""
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_all([Card('C', '2')])
    assert len(hand.cards) == 3


def test_hand_has_cards_no():
    """Check empty Hand has cards"""
    hand = Hand()
    assert not hand.has_cards


def test_hand_has_cards_yes():
    """ Check Hand has some cards."""
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.has_cards


def test_hand_take_top_check():
    """Take top card of hand"""
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    top_card = hand.take_top()
    assert str(top_card) == str(card1)


def test_hand_take_top_len_check_after_pop():
    """Hand len decreases after take_top"""
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    hand.take_top()
    assert len(hand.cards) == 1


def test_hand_take_top_has_only_1_card():
    """ Hand has only one card. take_top gives empty hand."""
    hand = Hand()
    card1 = Card('H', '5')
    hand.add_card(card1)
    top_card = hand.take_top()
    assert len(hand.cards) == 0
    assert str(top_card) == str(card1)


def test_hand_take_top_of_empty_hand():
    """Assert IndexError for empty hand, when take_top ran"""
    with pytest.raises(IndexError):
        hand = Hand()
        hand.take_top()
