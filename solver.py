from game import Game
from player import Player
import sys
import os
import time
from grid import *
from solver_functions import *

def solve(mode):
    #Initialize Game
    player = Player()
    game = Game(sys.argv[1], player)
    player.link_game = game
    #Initialize empty lists
    game_state_list = [GameState(game)] #Store game states to visit
    visited_list = [GameState(game)] #Store visited game states
    solutions_list = [] #Stores a list of solutions
    solution_found = False

    #Solving loop

    n = 0
    while True:
        n += 1
        
        if len(game_state_list) == 0:
            os.system("clear")
            print(f"Solving complete. {n} possible game states examined.")
            print()
            print(game.display)
            break

        os.system("clear")
        print("Solving" + (n%10)*".")
        print()
        print(game.display)
        
        time.sleep(0.05)
        
        #Take the first object in the list if using BFS, take the last if using DFS.
        if mode == ("BFS"):
            game_state = game_state_list[0]
            game_state_list = game_state_list[1:]
        elif mode == ("DFS"):
            game_state = game_state_list[-1]
            game_state_list = game_state_list[:-1]
        
        #Change current game state to the one picked out from above
        game_state.resume_game(game)
        
        #Record solution if game is won
        if game.won == True:
            solutions_list.append(copy_list(game.moves_made))
            solution_found = True
        
        #Find all the possible neighbouring moves that the game could make from current game state
        game_state.neighbours = find_neighbours(game, game_state)
        for neighbour in game_state.neighbours:
            if game_state_visited(neighbour, visited_list) == False:
                visited_list.append(neighbour)
                game_state_list.append(neighbour)
        
    #If a solution was found, print out number of moves, moves made and return true
    if solution_found == True:
        shortest_solution = []
        shortest_solution_number = len(solutions_list[0])
        for solution in solutions_list:
            if len(solution) <= shortest_solution_number:
                shortest_solution_number = len(solution)
                shortest_solution = solution
        print(f"Path has {shortest_solution_number} moves.")
        moves_made_str = ""
        i = 0
        for move in shortest_solution:
            i += 1
            if i < len(shortest_solution):
                moves_made_str += " " + move + ","
            else:
                moves_made_str += " " + move

        print(f"Path:{moves_made_str}")
        return True
    else:
        return False

#If there were no possible paths, print that
if __name__ == "__main__":
    found_solution = solve(sys.argv[2])
    if found_solution == True:
        pass
    else:
        print("There is no possible path.")


