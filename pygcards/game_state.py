# -*- coding: utf-8 -*-

class GameState:

    def __init__(self, history=[], errors=[], players=[]):
        self.history = history
        self.game_over = False
        self.winner = None
        errors = []
        self.players = players

