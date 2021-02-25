from game import Game
from player import Player
import os
import sys

#Initialize the player and game
p = Player()
g = Game(sys.argv[1], p)


while True:
    #Display the game
    os.system("clear")
    print(g.display)
    print("")

    #Display in-game messages
    if g.hit_wall == True:
        print("You walked into a wall.")
        print("")
    if g.found_water == True:
        print("You've found a bucket of water!")
        print("")
    if g.fire_extinguished == True:
        print("You have used a bucket of water to extinguish the flames!")
        print("")
    if g.has_teleported == True:
        print("Teleport successful!")
        print("")
    if g.invalid_move == True:
        print("Invalid move. Enter a valid move: (w, a, s, d, e, q).")
        print("")

    #If won, print out number of moves, the moves made and the win message
    if g.won == True:
        print("")
        print(f"You win!")
        print("")
        if len(g.moves_made) == 1:
            print(f"You made {g.num_moves} move.")
        else:
            print(f"You made {g.num_moves} moves.")
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

    #If lost, print out the print out number of moves, the moves made and the loss message
    if g.lost == True:
        print("")
        print("You have stepped into fire without water and died.")
        print("")
        if len(g.moves_made) == 1:
            print(f"You made {g.num_moves} move.")
        else:
            print(f"You made {g.num_moves} moves.")
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
    
    #Get user input
    movement_input = input("Input a move: ")

    #Can uncomment the below to run while clearing previous game displays
    #os.system("clear")

    #Take user input, quit if 'q', else pass it to the player object
    if movement_input == "q":
        print("")
        print("Bye!")
        break
    p.move(movement_input.lower())

    #Record number of moves and moves made
    if g.hit_wall == True or g.invalid_move == True:
        continue #skip recording moves if we hit a wall or make an invalid move
    g.num_moves += 1
    g.moves_made.append(movement_input.lower())
    
    