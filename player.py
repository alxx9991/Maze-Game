from grid import *
from game_parser import read_lines
class Player:
    def __init__(self):
        self.game = game
        self.grid = self.game.grid
        self.display = 'A'
        self.coordinate = grid_start(self.grid)
        self.row = self.coordinate.get_row()
        self.col = self.coordinate.get_col()
        self.num_water_buckets = 0

    def move(self, move):
        if move == 'a':
            self.game.game_move('a')
        elif move == 'd':
            self.game.game_move('d')
        elif move == 's':
            self.game.game_move('s')
        elif move == 'w':
            self.game.game_move('w')
        elif move == 'e':
            self.game.game_move('e')
        elif move == "q":
            self.game.game_move('q')


