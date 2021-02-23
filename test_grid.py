from grid import grid_to_string
from game_parser import *
from game import *
from player import *

def test_grid():
    #positive test case: board_simple.txt
    player = Player()
    game = Game("board_simple.txt", player)
    
    assert grid_to_string(read_lines("board_simple.txt"), player) == "**A**\n*   *\n**Y**\n\nYou have 0 water buckets."
    
    player = Player()
    game = Game("board_super_hard.txt", player)

    assert grid_to_string(read_lines("board_super_hard.txt"), player) == "*A*************\n*       2 *  W*\n* *** ** **** *\n* * WW*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n*W**W***   FFF*\n* 1********FFF*\n*************Y*\n\nYou have 0 water buckets."

def test_grid_start():
    #positive test cases
    player = Player()
    game = Game("board_medium.txt", player)

    assert grid_start(game.grid).get_row() == 0, "Starting cell incorrectly found"
    assert grid_start(game.grid).get_col() == 2, "Starting cell incorrectly found"

    player = Player()
    game = Game("board_hard.txt", player)

    assert grid_start(game.grid).get_row() == 0, "Starting cell incorrectly found"
    assert grid_start(game.grid).get_col() == 1, "Starting cell incorrectly found"

def test_other_teleport():
    player = Player()
    game = Game("simple_teleport.txt", player)
    
    #test single teleport
    assert other_teleport(game.grid, "1", 1, 1).get_row() == 1, "Matching teleport pad location not found"
    assert other_teleport(game.grid, "1", 1, 1).get_col() == 3, "Matching teleport pad location not found"

    assert other_teleport(game.grid, "1", 1, 3).get_row() == 1, "Matching teleport pad location not found"
    assert other_teleport(game.grid, "1", 1, 3).get_col() == 1, "Matching teleport pad location not found"
    
    #test multiple teleports
    player = Player()
    game = Game("board_super_hard.txt", player)

    assert other_teleport(game.grid, "2", 1, 8).get_row() == 5
    assert other_teleport(game.grid, "2", 1, 8).get_col() == 3

    assert other_teleport(game.grid, "1", 7, 2).get_row() == 3
    assert other_teleport(game.grid, "1", 7, 2).get_col() == 10

def run_tests():
    test_grid()
    test_grid_start()
    test_other_teleport()

run_tests()