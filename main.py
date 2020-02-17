import pygame
import player

print('''1. Knight
2. Assassin
3. Mage''')

build = (int(input("Which build do you wish to chose?: ")))

if build == 1:
    player = player.Knight()

if build == 2:
    player = player.Assassin()

if build == 3:
    player = player.Mage()

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
    player.draw(win)
    pygame.display.update()


# This is main game loop
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (player.x_position - player.dex) >= 0:
        player.x_position -= player.dex
        player.walk_left = True
        player.walk_right = False
        player.walk_up = False
        player.walk_down = False
    elif keys[pygame.K_RIGHT] and (player.x_position + player.dex) <= 1499:
        player.x_position += player.dex
        player.walk_left = False
        player.walk_right = True
        player.walk_up = False
        player.walk_down = False
    elif keys[pygame.K_UP] and (player.y_position - player.dex) >= 0:
        player.y_position -= player.dex
    elif keys[pygame.K_DOWN] and (player.y_position + player.dex) <= 799:
        player.y_position += player.dex
    else:
        player.walk_left = False
        player.walk_right = False
        player.walk_up = False
        player.walk_down = False

        player.walk_count = 0

    redraw_game_window()

pygame.quit()
