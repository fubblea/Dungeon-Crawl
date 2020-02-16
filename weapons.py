class Weapon:

    def __init__(self, w_range, damage, durability):
        self.w_range = w_range
        self.damage = damage
        self.durability = durability

    def use(self):
        self.durability -= 1


class Sword(Weapon):

    def __init__(self):
        Weapon.__init__(self, 10, 20, 100)
