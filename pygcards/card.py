class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank

    def is_ace(self):
        return self.rank == 'A'

    def to_string(self):
        return self.suit + str(self.rank)
