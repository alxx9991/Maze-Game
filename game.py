from game_parser import read_lines
from grid import *
from player import Player
from cells import *

class Game:
    def __init__(self, filename, player):
        self.grid = read_lines(filename)
        self.moves = 0
        self.won = False
        self.lost = False
        self.moves_made = []
        self.player = player
        self.player_coordinate = grid_start(self.grid)
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()
        self.player_water_buckets = 0
        self.display = grid_to_string(self.grid, self.player)

        


    def game_move(self, move): #Game move will receive player input. Check if move was valid. If it was, it will update the game accordingly, then update the player class.

        #Implement move checking - check for edge of the map, then check for wall.
        invalid_move = False #Assume move to be valid unless proven otherwise
        hit_wall = False #Check if we hit a wall
        if move == "a":
            if self.player_col == 0: #Check if we are currently on the left most column
                invalid_move = True
                print("Ur walking off the map")#DELETE
                
            elif is_wall(self.player_row, self.player_col - 1, self.grid) == True: #Check if the intended position is a wall
                invalid_move = True
                hit_wall = True
            else:
                self.player_coordinate.col -= 1

        elif move == "d":
            if self.player_col == grid_length(self.grid)-1: #Check if we are currently on the right most column
                invalid_move = True
                print("Ur walking off the map")
                
            elif is_wall(self.player_row, self.player_col + 1, self.grid) == True:
                invalid_move = True
                hit_wall = True
            else:
                self.player_coordinate.col += 1

        elif move == "w":
            if self.player_row == 0: #Check if we are currently on the top row
                invalid_move = True
                print("Ur walking off the map")#DELETE
                
            elif is_wall(self.player_row - 1, self.player_col, self.grid) == True:
                invalid_move = True
                hit_wall = True
            else:
                self.player_coordinate.row -= 1

        elif move == "s":
            if self.player_row == grid_height(self.grid) -1: #Check if we are currently on the bottom row
                invalid_move = True
                print("Ur walking off the map") #DELETE
                
            elif is_wall(self.player_row + 1, self.player_col, self.grid) == True:
                invalid_move = True
                hit_wall = True
            else:
                self.player_coordinate.row += 1

        elif move == "e":
            pass

        elif move == "q":
            self.lost = True

        else:
            print ("Invalid input") #Fix this to a proper error message
        
        
        
        #Update player attribute column and row
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()

        #Update player class column and row
        self.player.coordinate = self.player_coordinate
        self.player.row = self.player.coordinate.get_row()
        self.player.col = self.player.coordinate.get_col()
        

        #Step function to activate cell - prevents teleport by walking into a wall
        if hit_wall == False:
            self.grid[self.player_row][self.player_col].step(self)

        #Update game player_column and row in case of a teleport
        
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()
        
        #Update player coordinate, column and row position in case of a teleport
        self.player.coordinate = self.player_coordinate
        self.player.row = self.player.coordinate.get_row()
        self.player.col = self.player.coordinate.get_col()



        self.display = grid_to_string(self.grid, self.player)

        #Update player water buckets.
        self.player.num_water_buckets = self.player_water_buckets
        





