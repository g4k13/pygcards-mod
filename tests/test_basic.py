# -*- coding: utf-8 -*-

from .context import pygcards

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.deck = pygcards.Deck()

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_deck_has_52_cards(self):
        self.assertTrue(len(self.deck.deck) == 52)

    def test_deck_shuffles_cards(self):
        card_one = self.deck.deck[1]
        self.deck.shuffle_deck()
        card_two = self.deck.deck[2]
        self.assertTrue(card_one is not card_two)

    def test_card_identifies_as_ace(self):
        ace_card = pygcards.Card('♦', 'A')
        self.assertTrue(ace_card.is_ace())
    
    def test_deck_can_deal_to_hand(self):
        hand = pygcards.Hand(self.deck.deal(4)) 
        self.assertTrue(len(hand.cards) == 4)

if __name__ == '__main__':
    unittest.main()
