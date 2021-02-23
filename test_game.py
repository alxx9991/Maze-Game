from game import Game
from player import Player

def test_game():
    player = Player()
    game = Game("board_hard.txt", player)
    game.game_move("d")
    assert game.hit_wall == True, "Hit wall not recorded"
    game.game_move("s")
    assert game.hit_wall == False, "Hit wall recorded"

    #Negative test case - invalid move
    game.game_move("k")
    assert game.invalid_move == True, "Invalid move not recorded"
    
    #Edge test case - one move win
    player = Player()
    game = Game("board_XY.txt", player)
    game.game_move("d")
    assert game.won == True, "Game not won"


def run_tests():
    test_game()

run_tests()