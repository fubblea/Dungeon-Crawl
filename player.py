# TODO Add comments explaining whats happening
# TODO Finish methods for Knight and Rogue
class Player:

    def __init__(self, hp, dex):
        self.hp = hp
        self.dex = dex  # Dexterity. How fast the player moves

        # Description of the character
        self.width = 10
        self.height = 20
        self.x_position = 50
        self.y_position = 50
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0


# Animating the characters
class Knight(Player):

    def __init__(self):
        import pygame

        Player.__init__(self, 100, 30)

        self.idle = pygame.image.load('data/sprites/player/Knight/Idle/idle1.png')
        self.walk_right = [pygame.image.load('data/sprites/player/Knight/Walk/walk1.png'),
                           pygame.image.load('data/sprites/player/Knight/Walk/walk2.png'),
                           pygame.image.load('data/sprites/player/Knight/Walk/walk3.png'),
                           pygame.image.load('data/sprites/player/Knight/Walk/walk4.png'),
                           pygame.image.load('data/sprites/player/Knight/Walk/walk5.png'),
                           pygame.image.load('data/sprites/player/Knight/Walk/walk6.png')]
        self.walk_left = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk4.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk5.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Walk/walk6.png'), True, False)]

        self.walk_up = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Climb/climb1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Climb/climb3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Knight/Climb/climb4.png'), True, False)]

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
        import pygame
        Player.__init__(self, 75, 50)

        self.idle = pygame.image.load('data/sprites/player/Rogue/Idle/idle1.png')
        self.walk_right = [pygame.image.load('data/sprites/player/Rogue/Walk/walk1.png'),
                           pygame.image.load('data/sprites/player/Rogue/Walk/walk2.png'),
                           pygame.image.load('data/sprites/player/Rogue/Walk/walk3.png'),
                           pygame.image.load('data/sprites/player/Rogue/Walk/walk4.png'),
                           pygame.image.load('data/sprites/player/Rogue/Walk/walk5.png'),
                           pygame.image.load('data/sprites/player/Rogue/Walk/walk6.png')]
        self.walk_left = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk4.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk5.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Walk/walk6.png'), True, False)]

        self.walk_up = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb4.png'), True, False)]

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


class Mage(Player):

    def __init__(self):
        import pygame
        Player.__init__(self, 130, 15)

        self.idle = pygame.image.load('data/sprites/player/Mage/Idle/idle1.png')
        self.walk_right = [pygame.image.load('data/sprites/player/Mage/Walk/walk1.png'),
                           pygame.image.load('data/sprites/player/Mage/Walk/walk2.png'),
                           pygame.image.load('data/sprites/player/Mage/Walk/walk3.png'),
                           pygame.image.load('data/sprites/player/Mage/Walk/walk4.png'),
                           pygame.image.load('data/sprites/player/Mage/Walk/walk5.png'),
                           pygame.image.load('data/sprites/player/Mage/Walk/walk6.png')]
        self.walk_left = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk4.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk5.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Walk/walk6.png'), True, False)]

        self.walk_up = [
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb1.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb4.png'), True, False)]

    def draw(self, win):
        if self.walk_count + 1 >= 18:
            self.walk_count = 0

        if self.left:
            win.blit(self.walk_left[self.walk_count // 3], (self.x_position, self.y_position))
            self.walk_count += 1
        elif self.right:
            win.blit(self.walk_right[self.walk_count // 3], (self.x_position, self.y_position))
            self.walk_count += 1
        elif self.up:
            win.blit(self.walk_up[self.walk_count // 5], (self.x_position, self.y_position))
            self.walk_count += 1
        else:
            win.blit(self.idle, (self.x_position, self.y_position))
