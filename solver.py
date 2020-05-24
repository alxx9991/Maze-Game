
from game import Game
from player import Player
import os
import sys
from grid import Coordinate


def solve(mode):
    #Initialize Game
    p = Player()
    g = Game(sys.argv[1], p)
    p.link_game = g
    #Initialize empty lists
    visited = [str(g.player_coordinate)]
    cell_list = []
    move_list = []

    while True:
        g.game_move("a")
        if g.hit_wall == True or g.lost == True or str(Coordinate(g.player_row, g.player_col)) in visited:
            print("Cant go a")
            pass
        else:
            g.game_move("d")
            cell_list.append("a")
            visited.append(str(Coordinate(g.player_row, g.player_col-1)))
        
        g.game_move("d")
        if g.hit_wall == True or g.lost == True or str(Coordinate(g.player_row, g.player_col+1)) in visited:
            print("Can't go d")
        else:
            g.game_move("a")
            cell_list.append("d")
            visited.append(str(Coordinate(g.player_row, g.player_col+1)))

        g.game_move("s")
        if g.hit_wall == True or g.lost == True or str(Coordinate(g.player_row, g.player_col)) in visited:
            print("Can't go s")
            pass
        else:
            g.game_move("w")
            cell_list.append("s")
            visited.append(str(Coordinate(g.player_row+1, g.player_col)))

        g.game_move("w")
        if g.hit_wall == True or g.lost == True or str(Coordinate(g.player_row, g.player_col)) in visited:
            print("Cant go w")
            pass
        else:
            g.game_move("s")
            cell_list.append("w")
            visited.append(str(Coordinate(g.player_row-1, g.player_col)))
        
        if len(cell_list) == 0:
            print("no solution")
            break
        
        if g.won == True:
            print("solution found")
        
        cell = cell_list[0]
        cell_list = cell_list[1:]

        print(g.display)
        print(g.player_coordinate)
        print(f"Computer input: {cell}")
        p.move(cell)
        move_list.append(cell)

        ###Printing in game messages
        if g.hit_wall == True:
            print("You walked into a wall. Oof!")
            print("")
        
        if g.found_water == True:
            print("Thank the Honourable Furious Forest, you've found a bucket of water!")
            print("")

        if g.fire_extinguished == True:
            print("With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")
            print("")
        if g.has_teleported == True:
            print("Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.")
        ### IN GAME MESSAGES ^

        
        print("")
        print(f"Moves made are {move_list}.")
        print(f"Next moves lined up are {cell_list}")
        input()


# if __name__ == "__main__":
#     solution_found = False
#     if solution_found:
#         pass
#         # Print your solution...
#     else:
#         print("There is no possible path.")

solve("BFS")
