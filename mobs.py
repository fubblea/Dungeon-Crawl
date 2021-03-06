class Mobs:

    def __init__(self, m_range, damage, durability):
        self.m_range = m_range
        self.damage = damage
        self.durability = durability

    def jump(self):
        self.m_range += 1


class Crook(Mobs):

    def __init__(self):
        Mobs.__init__(self, 30, 20, 50)

    def punch(self):
        self.durability += 1


class Pirate(Mobs):

    def __init__(self):
        Mobs.__init__(self, 50, 40, 100)

    def scream(self):
        self.damage += 1


class Boss(Mobs):

    def __init__(self):
        Mobs.__init__(self, 100, 100, 1000)

    def mandem(self):
        self.m_range += 5
        self.damage += 5
        self.durability += 5