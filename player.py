class Player:

    def __init__(self, hp, dex):
        self.hp = hp
        self.dex = dex  # Dexterity. How fast the player moves

        self.width = 10
        self.height = 20
        self.x_position = 50
        self.y_position = 50


class Knight(Player):

    def __init__(self):
        Player.__init__(self, 100, 20)

# TODO Make two more builds
