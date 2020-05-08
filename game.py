from game_parser import read_lines
from grid import *
from player import Player


class Game:
    def __init__(self, filename):
        self.grid = read_lines(filename)
        self.moves = 0
        self.won = False
        self.lost = False
        self.moves_made = []
        self.player_position = grid_start(self.grid) #Set player coordinate to the start cell



    def game_move(self, move): #Move the player coordinate according to player input
        if move == 's':
            if self.player_position[0] == grid_height(self.grid)-1:
                print("Oof u walked into a wall")
            else:
                self.player_position[0] += 1
        elif move == 'a':
            if self.player_position[1] == 0:
                print("Oof u walked into a wall")
            else:
                self.player_position[1] -= 1
        elif move == 'w':
            if self.player_position[0] == 0:
                print("Oof u walked into a wall")
            else:
                self.player_position[0] -= 1
        elif move == 'd':
            if self.player_position[1] == grid_length(self.grid) -1 :
                print("Oof u walked into a wall")
            else:
                print("left")
                self.player_position[1] += 1
        i = self.player_position[0]
        j = self.player_position[1]

        self.grid[i][j].step(self)
        
        pass

a = Game("board_simple.txt")

assert a.player_position == [0,2]
