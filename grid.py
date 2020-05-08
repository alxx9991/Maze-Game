import cells
def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    pass

def grid_start(grid): #Looks for the starting cell and returns its coordinates 
    i = 0
    start_i = None
    start_j = None
    for row in grid:
        j = 0
        for cell in row:
            if str(cell) == "X":
                start_i = i
                start_j = j
            j += 1
        i += 1
    return [start_i,start_j]
    
def grid_end(grid): #Looks for the ending cell and returns its coordinates 
    end_coordinate = []
    i = 0
    for row in grid:
        j = 0
        for cell in grid:
            if cell == "Y":
                end_i = i
                end_j = j
            j += 1
        i += 1
    return [end_i,end_j]

def grid_length(grid): #Returns an integer representing the number of columns
    grid_length = len(grid[0])
    return grid_length

def grid_height(grid): #Returns an integer representing the number of rows
    grid_height = len(grid)
    return grid_height

