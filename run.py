from game import Game
import os
import sys

test_game = Game("board_simple.txt")



while test_game.won == False and test_game.lost == False:
    print(test_game.player_position)
    movement_input = input("Make a move (wasd): ")
    if movement_input == 'q':
        test_game.lost = True
        print("You lose cos u gave up")
    test_game.game_move(movement_input)