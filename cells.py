import grid
class Start:
    def __init__(self):
        self.display = 'X'
    def __str__(self):
        return self.display
    def step(self, game):
        pass


class End:
    def __init__(self):
        self.display = 'Y'
    def __str__(self):
        return self.display
    def step(self, game):
        game.won = True
        pass


class Air:
    def __init__(self):
        self.display = ' '
    def __str__(self):
        return self.display
    def step(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'
    def __str__(self):
        return self.display
    def step(self, game):
        pass


class Fire:
    def __init__(self):
        self.display = 'F'
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
        self.display = 'W'
    def __str__(self):
        return self.display
    def step(self, game):
        game.player_water_buckets += 1
        game.grid[game.player_row][game.player_col] = Air()
        game.found_water = True


class Teleport:
    def __init__(self, character, i, j):
        self.display = character
        self.row = i
        self.col = j
    def __str__(self):
        return self.display
    def step(self, game):
        game.player_coordinate.row = grid.other_teleport(game.grid, self.display, self.row, self.col).get_row()
        game.player_coordinate.col = grid.other_teleport(game.grid, self.display, self.row, self.col).get_col()
        game.has_teleported = True

