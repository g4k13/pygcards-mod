# -*- coding: utf-8 -*- 
from random import shuffle
from .card import Card

class Deck:
    def __init__(self):
        self.suits = ['♦', '♣', '♠', '♥']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)

    def get_suits(self):
        return self.suits

    def get_ranks(self):
        return self.ranks

    def deal(self, num_of_cards):
        dealt = self.cards[0:num_of_cards]
        self.cards = self.cards[num_of_cards:-1]
        return dealt

    def show_deck(self):
        for card in self.cards:
            print(card.to_string())
