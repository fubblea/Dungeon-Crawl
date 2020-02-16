class Weapon:

    def __init__(self, w_range, damage, durability):
        self.w_range = w_range
        self.damage = damage
        self.durability = durability

    def use(self):
        self.durability = self.durability - 1


class Sword(Weapon):

    def __init__(self):
        self.range = 10
        self.damage = 20
        self.durability = 100
