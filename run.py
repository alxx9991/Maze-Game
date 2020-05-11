from game import Game
from player import Player
import os
import sys

p = Player()
test_game = Game(sys.argv[1], p)


while test_game.won == False and test_game.lost == False:
    print(test_game.display)
    print(f"Number of water buckets: {test_game.player_water_buckets}")
    movement_input = input("Make a move (wasd): ")
    os.system("clear")
    p.move(movement_input)
    
    