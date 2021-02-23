from game_parser import read_lines
from grid import *
from player import Player
from cells import *

class Game:
    def __init__(self, filename, player):
        #Initialize game attributes
        self.grid = read_lines(filename)
        self.player = player
        self.display = grid_to_string(self.grid, self.player)
        self.player_coordinate = grid_start(self.grid)
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()
        self.player_water_buckets = 0
        
        #Initialize move trackers
        self.num_moves = 0
        self.moves_made = []
        
        #Move effects
        self.hit_wall = False
        self.fire_extinguished = False
        self.has_teleported = False
        self.invalid_move = False
        self.found_water = False
        self.won = False
        self.lost = False
        self.consecutive_waits = 0 #Used to keep solver waiting too many times
        
        #Initialize player attributes
        self.player.game = self
        self.player.coordinate = self.player_coordinate
        self.player.col = self.player_col
        self.player.row = self.player_row
        
    
    def game_move(self, move): #Game move will receive player input. Check if move was valid. If it was, it will update the game accordingly, then update the player class.

        #Implement move checking - check for edge of the map, then check for wall. 
        self.hit_wall = False #Check if we hit a wall
        self.found_water = False #Check if we found water
        self.fire_extinguished = False #Check if we extinguished fire
        self.has_teleported = False #Check if we just teleported
        self.invalid_move = False #Check if player entered invalid input (e.g. "L")
        
        #Receive player input, activate cell step function, update the game accordingly
        if move == "a":
            if self.player_col == 0: #Check if we are currently on the left most column
                self.hit_wall = True
                
            elif is_wall(self.player_row, self.player_col - 1, self.grid) == True: #Check if the intended position is a wall
                self.hit_wall = True

            else:
                self.player_coordinate.col -= 1
                self.consecutive_waits = 0

        elif move == "d":
            if self.player_col == grid_length(self.grid)-1: #Check if we are currently on the right most column
                self.hit_wall = True
                
            elif is_wall(self.player_row, self.player_col + 1, self.grid) == True:
                self.hit_wall = True

            else:
                self.player_coordinate.col += 1
                self.consecutive_waits = 0

        elif move == "w":
            if self.player_row == 0: #Check if we are currently on the top row
                self.hit_wall = True
                
            elif is_wall(self.player_row - 1, self.player_col, self.grid) == True:
                self.hit_wall = True

            else:
                self.player_coordinate.row -= 1
                self.consecutive_waits = 0

        elif move == "s":
            if self.player_row == grid_height(self.grid) -1: #Check if we are currently on the bottom row
                self.hit_wall = True
                
            elif is_wall(self.player_row + 1, self.player_col, self.grid) == True:
                self.hit_wall = True

            else:
                self.player_coordinate.row += 1
                self.consecutive_waits = 0

        elif move == "e":
            self.consecutive_waits += 1
            pass

        elif move == "q": #The run.py file will handle this case
            pass

        else:
            self.invalid_move = True

        #Update player attribute column and row
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()

        #Update player class column and row
        self.player.coordinate = self.player_coordinate
        self.player.row = self.player.coordinate.get_row()
        self.player.col = self.player.coordinate.get_col()
        
        #Step function to activate cell - prevents teleport by walking into a wall
        if self.hit_wall == False:
            self.grid[self.player_row][self.player_col].step(self)

        #Update game player_column and row in case of a teleport
        self.player_col = self.player_coordinate.get_col()
        self.player_row = self.player_coordinate.get_row()
        
        #Update player coordinate, column and row position in case of a teleport
        self.player.coordinate = self.player_coordinate
        self.player.row = self.player.coordinate.get_row()
        self.player.col = self.player.coordinate.get_col()


        #Update player water buckets.
        self.player.num_water_buckets = self.player_water_buckets
        self.display = grid_to_string(self.grid, self.player)
        
        

    




