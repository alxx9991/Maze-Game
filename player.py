from grid import *
from game_parser import read_lines
class Player: #Player attributes will be properly initialized by the game object
    def __init__(self):
        self.display = '\U0001F64A'
        self.game = None
        self.grid = None
        self.coordinate = None
        self.row = None
        self.col = None
        self.num_water_buckets = 0
    
    def move(self, move):
        self.game.game_move(move)
        


