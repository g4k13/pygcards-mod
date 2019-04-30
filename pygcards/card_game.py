# -*- coding: utf-8 -*- 
from pygcards import Deck

class CardGame:

    def __init__(self, deck=None, players=None, dealer=None, gamestate=None):
        self.deck = deck
        self.gamestate = gamestate
        self.players = players
        self.dealer = dealer

    def log(self, item):
        print(item)
        print("***************")

    @staticmethod
    def score(hand):
        return None

