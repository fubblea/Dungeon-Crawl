import pygame
import player

name = (str(input("Enter your name: ")))

print("1. Knight")
# TODO complete for other builds

build = (int(input("Which build?: ")))

if build == 1:
    player = player.Knight(name)
# TODO complete for other builds

screenWidth = 1500
screenHeight = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Dungeon Crawl")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # TODO Don't let the player go off the screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x_position -= player.dex
    if keys[pygame.K_RIGHT]:
        player.x_position += player.dex
    if keys[pygame.K_UP]:
        player.y_position -= player.dex
    if keys[pygame.K_DOWN]:
        player.y_position += player.dex

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (player.x_position, player.y_position, player.width, player.height))
    pygame.display.update()

pygame.quit()
