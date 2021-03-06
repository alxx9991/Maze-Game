
#Takes a grid and a player, converts it into a string that is displayable
def grid_to_string(grid, player):
    output_list = []
    i = 0
    for row in grid: #Convert objects in a list to strings in a list 
        output_row_list = []
        for cell in row:
            output_row_list.append(cell.display)
        output_row_list.append("\n")
        output_list.append(output_row_list)
        i += 1
    if not player.row:
        output_list[grid_start(grid).get_row()][grid_start(grid).get_col()] = '\U0001F64A'
    else:
        output_list[player.row][player.col] = '\U0001F64A'
    
    output_string = ""
    for row in output_list:
        for cell in row:
            output_string += cell
    
    if player.num_water_buckets == 1:
        output_string += '\n' + f"You have {player.num_water_buckets} water bucket."
    else:
        output_string += '\n' + f"You have {player.num_water_buckets} water buckets."

    return output_string

def grid_start(grid): #Looks for the starting cell and returns its coordinates 
    i = 0
    number_of_Xs = 0
    start_i = None
    start_j = None
    for row in grid:
        j = 0
        for cell in row:
            if str(cell) == '\U0001F6A9':
                start_i = i
                start_j = j
                number_of_Xs +=1
            j += 1
        i += 1
    if number_of_Xs == 0 or number_of_Xs > 1:
        raise ValueError(f"Expected 1 starting position, got {number_of_Xs}")

    return Coordinate(start_i, start_j)

def other_teleport(grid, number, own_row, own_col): #Looks for the other teleport cell and returns its coordinates 
    i = 0
    teleport_i = None
    teleport_j = None

    for row in grid:
        j = 0
        for cell in row:
            if str(cell) == number and (not(i == own_row and j == own_col)):
                teleport_i = i
                teleport_j = j
            j += 1
        i += 1
    return Coordinate(teleport_i, teleport_j)

def grid_length(grid): #Returns an integer representing the number of columns
    grid_length = len(grid[0])
    return grid_length

def grid_height(grid): #Returns an integer representing the number of rows
    grid_height = len(grid)
    return grid_height

def is_wall(row, col, grid): #Determine if given row and column coordinate contains a wall.
    i = row
    j = col
    if str(grid[i][j]) == '\U0001F7E6':
        return True
    else:
        return False

#Coordinate class to keep the coordinate things organised
class Coordinate:
    def __init__(self, row, col):
        self.col = col
        self.row = row
    
    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col

    def get_coordinate(self):
        return [self.row, self.col]

    def __str__(self):
        return f"({self.row}, {self.col})"

