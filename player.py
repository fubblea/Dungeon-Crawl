class Player:

    def __init__(self, name, hp, dex):
        self.name = name
        self.hp = hp
        self.dex = dex

        self.width = 10
        self.height = 20
        self.x_position = 50
        self.y_position = 50


class Knight(Player):

    def __init__(self, name):
        Player.__init__(self, name, 100, 20)

# TODO Make two more builds
