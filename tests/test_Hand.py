import pytest

from Cardlib import Hand, Card


def test_hand_empty():
    hand = Hand()
    assert len(hand.cards) == 0


def test_hand_add_card_1():
    hand = Hand()
    card = Card('D', '5')
    hand.add_card(card)
    assert len(hand.cards) == 1


def test_hand_add_card_multiple():
    hand = Hand()
    card = Card('D', '5')
    card1 = Card('C', '10')
    card2 = Card('H', 'A')
    hand.add_card(card)
    hand.add_card(card1)
    hand.add_card(card2)
    assert len(hand.cards) == 3


def test_hand_add_all_to_empty():
    cards = [Card('D', '5'), Card('C', '10'), Card('H', 'A'), Card('S', 'K')]
    hand = Hand()
    hand.add_all(cards)
    assert len(hand.cards) == len(cards)


def test_hand_add_all_to_non_empty():
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
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_all([Card('C', '2')])
    assert len(hand.cards) == 3


def test_hand_has_cards_no():
    hand = Hand()
    assert not hand.has_cards


def test_hand_has_cards_yes():
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.has_cards


def test_hand_take_top_check():
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    top_card = hand.take_top()
    assert str(top_card) == str(card1)


def test_hand_take_top_len_check_after_pop():
    hand = Hand()
    card1 = Card('H', '5')
    card2 = Card('S', 'J')
    hand.add_card(card1)
    hand.add_card(card2)
    hand.take_top()
    assert len(hand.cards) == 1


def test_hand_take_top_has_only_1_card():
    hand = Hand()
    card1 = Card('H', '5')
    hand.add_card(card1)
    top_card = hand.take_top()
    assert len(hand.cards) == 0
    assert str(top_card) == str(card1)


def test_hand_take_top_of_empty_hand():
    with pytest.raises(IndexError):
        hand = Hand()
        hand.take_top()
