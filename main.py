# TODO Add comments explaining whats happening
import pygame
import player

print('''1. Knight
2. Assassin
3. Mage''')

build = (int(input("Which build do you wish to chose?: ")))

if build == 1:
    user = player.Knight()

if build == 2:
    user = player.Assassin()

if build == 3:
    user = player.Mage()

# This creates the game window
screenWidth = 512
screenHeight = 512
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Crawl")

bg = pygame.image.load('data/bg.jpg')
clock = pygame.time.Clock()


def redraw_game_window():
    # This draws the player and updates it's position
    win.blit(bg, (0, 0))
    user.draw(win)
    pygame.display.update()


# This is main game loop
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (user.x_position - user.dex) >= 0:
        user.x_position -= user.dex
        user.left = True
        user.right = False
        user.up = False
        user.down = False
    elif keys[pygame.K_RIGHT] and (user.x_position + user.dex) <= 1499:
        user.x_position += user.dex
        user.left = False
        user.right = True
        user.up = False
        user.down = False
    elif keys[pygame.K_UP] and (user.y_position - user.dex) >= 0:
        user.y_position -= user.dex
        # TODO Implement for up
    elif keys[pygame.K_DOWN] and (user.y_position + user.dex) <= 799:
        user.y_position += user.dex
        # TODO Implement for down
    else:
        user.left = False
        user.right = False
        user.up = False
        user.down = False

        user.walk_count = 0

    redraw_game_window()

pygame.quit()
