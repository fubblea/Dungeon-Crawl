class Weapon:

    def __init__(self, w_range, damage, durability, speed):
        self.w_range = w_range
        self.damage = damage
        self.durability = durability
        self.speed = speed

    def use(self):
        self.durability -= 1


class Sword(Weapon):

    def __init__(self):
        Weapon.__init__(self, 10, 20, 100, 5)


class Dagger(Weapon):

    def __init__(self):
        Weapon.__init__(self, 5, 20, 100, 10)

    def throw(self):
        self.w_range = 50
