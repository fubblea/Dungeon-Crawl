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
screenWidth = 1500
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Crawl")


def redraw_game_window():
    # This draws the player and updates it's position
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (player.x_position, player.y_position, player.width, player.height))
    pygame.display.update()


# This is main game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # TODO Don't let the player go off the screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (player.x_position - player.dex) >= 0:
        player.x_position -= player.dex
    if keys[pygame.K_RIGHT] and (player.x_position + player.dex) <= 1499:
        player.x_position += player.dex
    if keys[pygame.K_UP] and (player.y_position - player.dex) >= 0:
        player.y_position -= player.dex
    if keys[pygame.K_DOWN] and (player.y_position + player.dex) <= 799:
        player.y_position += player.dex


    redraw_game_window()

pygame.quit()
