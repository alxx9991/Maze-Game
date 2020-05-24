from game import Game
from player import Player
import os
import sys

p = Player()
g = Game(sys.argv[1], p)
p.link_game = g


while True:
    print(g.display)
    print("")
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
        print("")
    if g.invalid_move == True:
        print("Please enter a valid move (w, a, s, d, e, q).")
        print("")
    if g.won == True:
        print("")
        print(f"You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
        print("")
        if len(g.moves_made) == 1:
            print(f"You made {g.moves} move.")
        else:
            print(f"You made {g.moves} moves.")
        moves_made_str = ""
        i = 0
        for move in g.moves_made:
            i += 1
            if i < len(g.moves_made):
                moves_made_str += " " + move + ","
            else:
                moves_made_str += " " + move
        if len(g.moves_made) == 1:
            print(f"Your move:{moves_made_str}")
        else:
            print(f"Your moves:{moves_made_str}")
        print("")
        print("=====================\n====== YOU WIN! =====\n=====================")
        break
    if g.lost == True:
        print("")
        print("You step into the fires and watch your dreams disappear :(.")
        print("")
        print("The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
        print("")
        if len(g.moves_made) == 1:
            print(f"You made {g.moves} move.")
        else:
            print(f"You made {g.moves} moves.")
        moves_made_str = ""
        i = 0
        for move in g.moves_made:
            i += 1
            if i < len(g.moves_made):
                moves_made_str += " " + move + ","
            else:
                moves_made_str += " " + move
        if len(g.moves_made) == 1:
            print(f"Your move:{moves_made_str}")
        else:
            print(f"Your moves:{moves_made_str}")
        print("")
        print("=====================\n===== GAME OVER =====\n=====================")
        break
    movement_input = input("Input a move: ")
    #os.system("clear")
    if movement_input == "q":
        print("")
        print("Bye!")
        break
    p.move(movement_input.lower())
    if g.hit_wall == True or g.invalid_move == True:
        continue #skip recording moves if we hit a wall or make an invalid move
    g.moves += 1
    g.moves_made.append(movement_input.lower())
    
    