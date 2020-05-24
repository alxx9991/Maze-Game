from grid import *
from game_parser import read_lines
class Player:
    def __init__(self):
        self.display = 'A'
        self.game = None
        self.grid = None
        self.coordinate = None
        self.row = None
        self.col = None
        self.num_water_buckets = 0
        self.game = None
        self.grid = None

    def move(self, move):
        self.game.game_move(move)
        


