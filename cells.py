import grid

#Contains all the cell classes

class Start:
    def __init__(self):
        self.display = '\U0001F6A9' #What the cell displays when the grid is printed out
    def __str__(self):
        return self.display
    def step(self, game): #How the cell affects the game if the cell is stepped on
        pass 

class End:
    def __init__(self):
        self.display = '\U0001F3C1'
    def __str__(self):
        return self.display
    def step(self, game):
        game.won = True
        pass

class Air:
    def __init__(self):
        self.display = '  '
    def __str__(self):
        return self.display
    def step(self, game):
        pass

class Wall:
    def __init__(self):
        self.display = '\U0001F7E6'
    def __str__(self):
        return self.display
    def step(self, game):
        pass

class Fire:
    def __init__(self):
        self.display = '\U0001F525'
    def __str__(self):
        return self.display
    def step(self, game):
        if game.player_water_buckets > 0:
            game.grid[game.player_row][game.player_col] = Air()
            game.player_water_buckets -= 1
            game.fire_extinguished = True
        else:
            game.lost = True

class Water:
    def __init__(self):
        self.display = '\U0001F4A7'
    def __str__(self):
        return self.display
    def step(self, game):
        game.player_water_buckets += 1
        game.grid[game.player_row][game.player_col] = Air()
        game.found_water = True

class Teleport:
    def __init__(self, character, i, j):
        self.display = character + " "
        self.row = i
        self.col = j
    def __str__(self):
        return self.display
    def step(self, game):
        game.player_coordinate.row = grid.other_teleport(game.grid, self.display, self.row, self.col).get_row()
        game.player_coordinate.col = grid.other_teleport(game.grid, self.display, self.row, self.col).get_col()
        game.has_teleported = True

