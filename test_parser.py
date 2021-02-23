from game_parser import read_lines
from cells import *


def test_read_lines():
    #test board_medium.txt: positive test case
    assert isinstance(read_lines("board_medium.txt")[0][2], Start), "Coordinate 0,2 is not a Start Cell"
    assert isinstance(read_lines("board_medium.txt")[5][4], End), "Coordinate 5,4 is not a End Cell"
    assert isinstance(read_lines("board_medium.txt")[1][1], Air), "Coordinate 1,1 is not a Air Cell"
    assert isinstance(read_lines("board_medium.txt")[0][5], Wall), "Coordinate 0,5 is not a Wall Cell"
    

    
    #test file with grid only made of Fire cells: edge case
    all_fire = True
    for row in read_lines("fire.txt"):
        for cell in row:
            if isinstance(cell, Fire) == False and isinstance(cell, Start) == False and isinstance(cell, End) == False:
                all_fire = False
    assert all_fire == True, "Non-fire (or start/end) cell detected."

    #test file with 4 teleports of the same number: negative test case
    value_error_caught = False
    try:
        read_lines("board_four_teleports.txt")
    except:
        ValueError
        value_error_caught = True
    assert value_error_caught == True
    

    #test file with just XY: edge case
    assert isinstance(read_lines("board_XY.txt")[0][0], Start), "Coordinate 0,0 is not a Start Cell"
    assert isinstance(read_lines("board_XY.txt")[0][1], End), "Coordinate 0,1 is not a End Cell"
def run_tests():
    test_read_lines()

run_tests()