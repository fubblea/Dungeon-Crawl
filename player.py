class Player:

    def __init__(self, hp, dex):
        self.hp = hp
        self.dex = dex  # Dexterity. How fast the player moves

        self.width = 10
        self.height = 20
        self.x_position = 50
        self.y_position = 50
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0


class Knight(Player):

    def __init__(self):
        import pygame

        Player.__init__(self, 100, 30)

        self.idle = pygame.image.load('data/sprites/player/Knight/Idle/idle1.png')
        self.walk_right = [pygame.image.load('data/sprites/player/Knight/Walk/walk1.png'), pygame.image.load('data/sprites/player/Knight/Walk/walk2.png'), pygame.image.load('data/sprites/player/Knight/Walk/walk3.png'), pygame.image.load('data/sprites/player/Knight/Walk/walk4.png'), pygame.image.load('data/sprites/player/Knight/Walk/walk5.png'), pygame.image.load('data/sprites/player/Knight/Walk/walk6.png')]
        self.walk_left = [pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk1.png'), True, False), pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk2.png'), True, False), pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk3.png'), True, False), pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk4.png'), True, False), pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk5.png'), True, False), pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk6.png'), True, False)]

    def draw(self, win):
        if self.walk_count + 1 >= 18:
            self.walk_count = 0

        if self.left:
            win.blit(self.walk_left[self.walk_count // 3], (self.x_position, self.y_position))
            self.walk_count += 1
        elif self.right:
            win.blit(self.walk_right[self.walk_count // 3], (self.x_position, self.y_position))
            self.walk_count += 1
        else:
            win.blit(self.idle, (self.x_position, self.y_position))

class Assassin(Player):

    def __init__(self):
        Player.__init__(self, 75, 50)

    # TODO Animate


class Mage(Player):

    def __init__(self):
        Player.__init__(self, 130, 15)

    # TODO Animate
