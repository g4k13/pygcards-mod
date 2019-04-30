# -*- coding: utf-8 -*-
from pygcards import CardGame
from pygcards import Player
from pygcards import Deck
import time
import re

class BlackJack(CardGame):
    
    def __init__(self):
        super().__init__(self)
        self.player_standing = False
        self.player_busted = False
        self.deck = Deck()
        self.players = [Player(self.score)]
        self.dealer = Player(self.score)

    @staticmethod
    def score(hand):
        score = 0
        aces = 0
        is_face = re.compile(r"[KQJ]")
        for card in hand.cards:
            value = 0
            if isinstance(card.rank, int):
                value = card.rank
            elif card.is_ace():
                aces += 1
            else:
                value = 10
            score += value
  
        ace_value = 0
        for i in range(aces):
            if (score + 11) > 21:
                ace_value += 1
            else:
                ace_value += 11
            score += ace_value

        return score

    def deal_cards(self, player, number):
        cards = self.deck.deal(number)
        player.add_cards(cards)
       
    def twentyone(self, player):
        return player.score() == 21

    def busts(self, player):
        self.player_busted = player.score() > 21
        return self.player_busted

    def hit(self, player):
        cards = self.deck.deal(1)
        player.add_cards(cards)
        time.sleep(2)
        self.show_cards(player)

    def stand(self, player):
        self.player_standing = True
        self.log("PLAYER STANDS: " + player.hand.to_string() + " : " + str(player.score()))

    def show_cards(self, player):
        self.log(player.hand.to_string() + ", SCORE: " + str(player.score()))

    def show_dealer_cards(self):
        self.log("DEALER'S HAND: " + self.dealer.hand.to_string() + ", SCORE: " + str(self.dealer.score()))

    def player_continues(self, player):
        return True if not self.player_standing and not self.busts(player) and not self.twentyone(player) else False

    def dealer_continues(self):
        return True if not self.busts(self.dealer) and not self.twentyone(self.dealer) and self.dealer.score() < 17 else False

    def play_game(self):
        self.log("\n\nWELCOME TO PYGCARDS::BLACKJACK")
        for player in self.players:
            self.log("One card for you")
            self.hit(player)
            self.log("One card for the dealer")
            self.hit(self.dealer)
            self.log("One card for you")
            self.hit(player)
            while(self.player_continues(player)):
                choices = {
                        "h" : lambda: self.hit(player),
                        "s" : lambda: self.stand(player),
                        "c" : lambda: self.show_cards(player),
                        "d" : lambda: self.show_dealer_cards()
                        }
                player_choice = input("Choose (h) hit, (s) stand, (c) see your hand, (d) see dealer's hand: ").strip()
                function = choices.get(player_choice, lambda: self.log("Invalid Choice")) 
                function()
            if self.twentyone(player):
                self.log("YOU WON, 21!")
            elif self.player_busted:
                self.log("YOU BUSTED: " + str(player.score()))
            else:
                self.log("DEALER'S TURN")
                self.hit(self.dealer)
                while(self.dealer_continues()):
                        self.log("DEALER HITS")
                        self.hit(self.dealer)
                if self.busts(self.dealer):
                    self.log("DEALER BUSTED, YOU WON!")
                elif self.twentyone(self.dealer):
                    self.log("YOU LOST, DEALER 21 :(")
                else:
                    self.log("YOUR SCORE: " + str(player.score()) + " , DEALER'S SCORE: " + str(self.dealer.score()))
                    if player.score() >= self.dealer.score():
                        self.log("YOU WON!")
                    else:
                        self.log("DEALER WON :(")

if __name__=='__main__':
    self.play_game()
