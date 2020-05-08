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
        pass


class Water:
    def __init__(self):
        self.display = 'W'
    def __str__(self):
        return self.display
    def step(self, game):
        pass


class Teleport:
    def __init__(self, number):
        self.display = number  # You'll need to change this!
    def __str__(self):
        return self.display
    def step(self, game):
        pass
