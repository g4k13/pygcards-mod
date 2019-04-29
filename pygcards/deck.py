from random import shuffle
from .card import Card

class Deck:
    def __init__(self):
        self.suits = ['♦', '♣', '♠', '♥']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.deck = [Card(suit, rank) for rank in self.ranks for suit in self.suits]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)

    def get_suits(self):
        return self.suits

    def get_ranks(self):
        return self.ranks

    def deal(self, num_of_cards):
        return self.deck[0:num_of_cards]
