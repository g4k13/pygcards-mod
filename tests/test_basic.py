# -*- coding: utf-8 -*-

from .context import pygcards
from pygcards import *
import unittest
import pdb


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.deck = pygcards.Deck()
        self.hand_random = Hand()
        self.hand_random.cards = self.deck.deal(3)
        self.hand_twenty = Hand()
        self.hand_twenty.cards = [Card('♦', 10), Card("♥","J")]
        self.hand_twentyone = Hand()
        self.hand_twentyone.cards = [Card('♦', 10), Card("♥","J"), Card("♥","A")]
        self.hand_busts = Hand()
        self.hand_busts.cards = [Card('♦', 10), Card("♥","J"), Card("♥","9")]
        self.black_jack = BlackJack()

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_black_jack_deck_has_52_cards(self):
        self.assertTrue(len(self.black_jack.deck.cards) == 52)

    def test_deck_can_deal_cards(self):
        self.assertTrue(len(self.deck.deal(2)) == 2)

    def test_card_identifies_as_ace(self):
        ace_card = pygcards.Card('♦', 'A')
        self.assertTrue(ace_card.is_ace())
    
    def test_deck_can_deal_to_hand(self):
        hand = pygcards.Hand(self.deck.deal(4)) 
        self.assertTrue(len(hand.cards) == 4)

    def test_blackjack_can_score_hand(self):
        self.assertTrue(BlackJack.score(self.hand_twenty) == 20)

    def test_blackjack_can_score_ace_right(self):
        self.assertTrue(BlackJack.score(self.hand_twentyone) == 21)

    def test_blackjack_has_player(self):
        self.assertTrue(len(self.black_jack.players) == 1)

    def test_player_can_score_hand(self):
        self.black_jack.players[0].hand = self.hand_twenty
        self.assertTrue(self.black_jack.players[0].score() == 20)

    def test_blackjack_can_tell_when_a_player_busts(self):
        self.black_jack.players[0].hand = self.hand_busts
        self.assertTrue(self.black_jack.busts(self.black_jack.players[0]))

    def test_blackjack_can_tell_when_a_player_has_twentyone(self):
        self.black_jack.players[0].hand = self.hand_twentyone
        self.assertTrue(self.black_jack.twentyone(self.black_jack.players[0]))

    def test_blackjack_player_can_hit(self):
        player = self.black_jack.players[0]
        card_count = len(player.hand.cards)
        self.black_jack.hit(player)
        self.assertTrue(len(player.hand.cards) == card_count + 1)
    
    def test_blackjack_can_tell_when_player_can_continue(self):
        self.black_jack.players[0].hand = self.hand_twenty
        self.assertTrue(self.black_jack.player_continues(self.black_jack.players[0]))

    def test_blackjack_hit_removes_card_from_deck(self):
        player = self.black_jack.players[0]
        num_of_cards = len(self.black_jack.deck.cards)
        self.black_jack.hit(player)
        num_after_hit = len(self.black_jack.deck.cards)
        self.assertTrue(num_of_cards > num_after_hit)

    def test_blackjack_play_game(self):
        self.black_jack.play_game()
        self.assertTrue(self.black_jack.player_standing or self.black_jack.player_busted)

if __name__ == '__main__':
    unittest.main()
