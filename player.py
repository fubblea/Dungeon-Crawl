

class Player:

    def __init__(self, hp, dex):
        self.hp = hp
        self.dex = dex  # Dexterity. How fast the player moves

        # Description of the character
        self.width = 128
        self.height = 128
        self.x_position = 50
        self.y_position = 50
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.walk_count = 0

    def draw(self, win):
        if self.walk_count + 1 >= 18:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                win.blit(self.walk_left[self.walk_count // 3], (self.x_position, self.y_position))
                self.walk_count += 1
            elif self.right:
                win.blit(self.walk_right[self.walk_count // 3], (self.x_position, self.y_position))
                self.walk_count += 1
            elif self.up:
                win.blit(self.walk_up[self.walk_count // 5], (self.x_position, self.y_position))
                self.walk_count += 1
            elif self.down:
                win.blit(self.idle, (self.x_position, self.y_position))
        else:
            if self.right:
                win.blit(self.walk_right[0], (self.x_position, self.y_position))
            elif self.left:
                win.blit(self.walk_left[0], (self.x_position, self.y_position))
            elif self.up:
                win.blit(self.walk_up[0], (self.x_position, self.y_position))
            else:
                win.blit(self.idle, (self.x_position, self.y_position))


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
            (pygame.image.load('data/sprites/player/Knight/Climb/climb2.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Climb/climb2.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Climb/climb3.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Climb/climb4.png'), True, False)]

        self.attack = [
            (pygame.image.load('data/sprites/player/Knight/Attack/attack0.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Attack/attack1.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Attack/attack2.png'), True, False),
            (pygame.image.load('data/sprites/player/Knight/Attack/attack3.png'), True, False), ]


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
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Rogue/Climb/climb4.png'), True, False)]

        self.attack = [
            (pygame.image.load('data/sprites/player/Rogue/Attack/Attack1.png'), True, False),
            (pygame.image.load('data/sprites/player/Rogue/Attack/Attack2.png'), True, False),
            (pygame.image.load('data/sprites/player/Rogue/Attack/Attack3.png'), True, False),
            (pygame.image.load('data/sprites/player/Rogue/Attack/Attack4.png'), True, False)]


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
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb2.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb3.png'), True, False),
            pygame.transform.flip(pygame.image.load('data/sprites/player/Mage/Climb/climb4.png'), True, False)]
