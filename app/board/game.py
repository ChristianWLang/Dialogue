#!/usr/bin/env python3
"""
Board game (Risk)
# Author: Christian Lang
"""


class Game:
    def __init__(self, players):

        try:
            self.players = int(players)
        except:
            raise Exception('Players must be passed as integer')

        if 2 <= self.players <= 6:
            raise Exception('Invalid number of players, must be between 2 - 6')

        army_sizes = {2: 40, 3: 35, 4: 30, 5: 25, 6: 20}
        self.army_size = army_sizes[self.players]

        self.territories = np.arange(42)
        self.continents = ''

        pass
