from game import Game
from player import Player
from grid import *

#This module contains all of the helper functions for the solver module. Originally I had it all in solver.py but it got a bit messy so I split it off.


#The two functions below are used to keep lists from changing when saving game states.
def copy_list(ls):
    new_ls = []
    for obj in ls:
        new_ls.append(obj)
    return new_ls

def copy_list_of_lists(ls):
    new_ls_of_ls = []
    for inside_ls in ls:
        new_ls_of_ls.append(copy_list(inside_ls))
    return new_ls_of_ls

#This class saves the attributes of the game which change as the game progresses. It also stores any neighbouring possible game states, which you can get to in one move.
class GameState: 
    def __init__(self, game):
        #Saving move effects
        self.hit_wall = game.hit_wall 
        self.found_water = game.found_water 
        self.fire_extinguished = game.fire_extinguished 
        self.has_teleported = game.has_teleported
        self.invalid_move = game.invalid_move
        self.won = game.won
        self.lost = game.lost
        self.consecutive_waits = game.consecutive_waits
        
        #Saving player coordinates/buckets
        self.player_col = game.player_col
        self.player_row = game.player_row
        self.player_water_buckets = game.player_water_buckets
        self.grid = copy_list_of_lists(game.grid)
        self.display = game.display
        
        #Save tracking attributes
        self.moves_made = copy_list(game.moves_made)
        self.num_moves = game.num_moves
        
        #Store neighbouring game states in a list
        self.neighbours = []
        
    #Resume game function can be used to switch the current game out with the game state that is specified.
    def resume_game(self, game):
        #Restore move effects
        game.hit_wall = self.hit_wall 
        game.found_water = self.found_water 
        game.fire_extinguished = self.fire_extinguished 
        game.has_teleported = self.has_teleported
        game.invalid_move = self.invalid_move
        game.won = self.won
        game.lost = self.lost
        game.consecutive_waits = self.consecutive_waits
        
        #Restore player coordinates/buckets
        game.player_coordinate = Coordinate(self.player_row, self.player_col)
        game.player_water_buckets = self.player_water_buckets

        #Restore tracking attributes
        game.num_moves = self.num_moves
        game.moves_made = copy_list(self.moves_made)
        game.grid = copy_list_of_lists(self.grid)
        game.display = self.display
    
        #Update game attributes: player col and row
        game.player_col = game.player_coordinate.get_col()
        game.player_row = game.player_coordinate.get_row()

        #Update player class column and row
        game.player.coordinate = game.player_coordinate
        game.player.row = game.player.coordinate.get_row()
        game.player.col = game.player.coordinate.get_col()

        #Update player water buckets
        game.player.num_water_buckets = game.player_water_buckets
        
def is_same_game_state(game_state_1, game_state_2):
    #This function is used to compare to game states to see if they are the same.
    #Compares:
    #Player row and column
    #Number of water buckets
    #Move effects - found water, fire extinguished, has teleported, won, lost, consecutive waits
    
    #Looks like a big mess, but it really just uses all the checks above
    ##If changing these, change the comments above as well
    if game_state_1.player_row == game_state_2.player_row and game_state_1.player_col == game_state_2.player_col and game_state_1.player_water_buckets == game_state_2.player_water_buckets and game_state_1.found_water == game_state_2.found_water and game_state_1.fire_extinguished == game_state_2.fire_extinguished and game_state_1.has_teleported == game_state_2.has_teleported and game_state_1.won == game_state_2.won and game_state_1.lost == game_state_2.lost and game_state_1.consecutive_waits == game_state_2.consecutive_waits:
        return True
    else:
        return False

#Takes a game state and checks it using above function on a list of game states already visited. If there is a match, return True
def game_state_visited(game_state_1, visited_list):
    for game_state_2 in visited_list:
        if is_same_game_state(game_state_1, game_state_2) == True:
            return True
        else:
            pass
    return False


#Takes a game state. Returns a list of neighbours of the game state.
def find_neighbours(game, game_state):
    temp_game_save = GameState(game) #Always restore this version of the game when returning
    neighbours_list = []
    
    game_state.resume_game(game) #Sets the game to the game state in question

    game.game_move("a")
    if game.hit_wall == True or game.lost == True:
        game_state.resume_game(game)
        pass
    else:
        neighbour = GameState(game)
        neighbour.moves_made.append("a")
        temp_game_save.resume_game(game)
        neighbours_list.append(neighbour)
    
    game.game_move("s")
    if game.hit_wall == True or game.lost == True:
        game_state.resume_game(game)
        pass
    else:
        neighbour = GameState(game)
        neighbour.moves_made.append("s")
        temp_game_save.resume_game(game)
        neighbours_list.append(neighbour)
    
    game.game_move("d")
    if game.hit_wall == True or game.lost == True:
        game_state.resume_game(game)
        pass
    else:
        neighbour = GameState(game)
        neighbour.moves_made.append("d")
        temp_game_save.resume_game(game)
        neighbours_list.append(neighbour)
    
    game.game_move("w")
    if game.hit_wall == True or game.lost == True:
        game_state.resume_game(game)
        pass
    else:
        neighbour = GameState(game)
        neighbour.moves_made.append("w")
        temp_game_save.resume_game(game)
        neighbours_list.append(neighbour)
    
    #Only allow wait as an option if the player has just teleported, and has not waited already
    if game.has_teleported == True and game.consecutive_waits < 1:
        game.game_move("e")
        if game.hit_wall == True or game.lost == True:
            game_state.resume_game(game)
            pass
        else:
            neighbour = GameState(game)
            neighbour.moves_made.append("e")
            temp_game_save.resume_game(game)
            neighbours_list.append(neighbour)
    
    #Restore original game state
    temp_game_save.resume_game(game)
    return neighbours_list