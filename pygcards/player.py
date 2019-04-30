# -*- coding: utf-8 -*- 
from pygcards import Hand

class Player:

    def __init__(self, score_fn):
        self.score_fn = score_fn
        self.hand = Hand()

    def score(self):
        return self.score_fn(self.hand)

    def winning_phrase(self):
        return "I WON!"

    def losing_phrase(self):
        return "I LOST!"

    def add_cards(self, cards):
        self.hand.add_cards(cards)


