class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add_cards(self, new_cards):
        self.cards = self.cards + new_cards

    def shuffle_hand(self):
        shuffle(self.cards)
