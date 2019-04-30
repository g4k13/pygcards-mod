# -*- coding: utf-8 -*- 

class Hand:
    def __init__(self, hand=[]):
        self.cards = hand

    def add_cards(self, new_cards):
        self.cards = self.cards + new_cards

    def shuffle_hand(self):
        shuffle(self.cards)

    def to_string(self):
        show = ""
        for card in self.cards:
            show += card.to_string()
            show += " "
        return show.strip()
