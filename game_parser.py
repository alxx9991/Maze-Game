from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

boardname = "board_simple.txt" #Change this to sys.argv later

def read_lines(filename):
    infile = open(boardname, 'r')
    lines = [] #Create empty list of lines
    i = 0
    #Create list of lines with new line characters stripped
    while True:
        line = str.strip(infile.readline())
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
    for row in cell_list:
        j = 0
        for character in row:
            if character == "X":
                cell_list[i][j] = Start()
            elif character == "Y":
                cell_list[i][j] = End()
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
            else:
                character = Teleport
            j += 1
        i += 1
    
    #Fix this when finished cell classes
    return cell_list
