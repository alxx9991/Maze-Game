from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from grid import Coordinate



def read_lines(filename):
    infile = open(filename, 'r')
    lines = [] #Create empty list of lines
    i = 0
    #Create list of lines with new line characters stripped
    while True:
        line = infile.readline()
        if line == "":
            break
        lines.append(line)
        i+=1
    
    return parse(lines) #Use parse function to turn list of lines into 2D list of cells
        


def parse(lines):
    cell_list = [] #Output list of cells - 2D cell list
    for line in lines: #For each line do the following
        i = 0
        ch_list = []
        for ch in line: #For each character in the line, append the character to a list representing that line
            ch_list.append(ch)
        line = ch_list.copy() #Replace line with said list
        cell_list.append(line) #Append output list with said line
    
    i = 0
    num_of_X = 0
    num_of_Y = 0
    teleport_list = []
    
    for row in cell_list:
        j = 0
        for character in row:
            if character == "\n":
                row.remove(character)
            elif character == "X":
                cell_list[i][j] = Start()
                num_of_X += 1
            elif character == "Y":
                cell_list[i][j] = End()
                num_of_Y += 1
            elif character == " ":
                cell_list[i][j] = Air()
            elif character == "*":
                cell_list[i][j] = Wall()
            elif character == "F":
                cell_list[i][j] = Fire()
            elif character == "W":
                cell_list[i][j] = Water()
            elif character == "Y":
                cell_list[i][j] = End()
            elif character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
                cell_list[i][j] = Teleport(character, i, j)
                teleport_list.append(character)
            else:
                raise ValueError(f"Bad letter in configuration file: {character}.")
            j += 1
        i += 1
        
    if num_of_X == 0 or num_of_X > 1:
        raise ValueError(f"Expected 1 starting position, got {num_of_X}.")
    if num_of_Y == 0 or num_of_Y > 1:
        raise ValueError(f"Expected 1 ending position, got {num_of_Y}.")
    for teleport_pad in range (1,10):
        if teleport_list.count(str(teleport_pad)) % 2 == 1:
            raise ValueError(f"Teleport pad {teleport_pad} does not have an exclusively matching pad.")

    #Fix this when finished cell classes
    return cell_list
