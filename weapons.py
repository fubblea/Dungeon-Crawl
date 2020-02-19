class Melee:

    def __init__(self, w_range, damage, durability, speed):
        self.w_range = w_range
        self.damage = damage
        self.durability = durability
        self.speed = speed

    def use(self):
        self.durability -= 1


class Sword(Melee):

    def __init__(self):
        Melee.__init__(self, 10, 20, 100, 5)


class Dagger(Melee):

    def __init__(self):
        Melee.__init__(self, 5, 20, 100, 10)


class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        import pygame

        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
