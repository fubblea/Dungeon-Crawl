# TODO Explain how I did the facing thing
# idk how you did the facing thing pls help
import pygame
import player

print('''1. Knight
2. Assassin
3. Mage''')

build = (int(input("Which build do you wish to chose?: ")))  # Asks the user to pick a character

if build == 1:
    user = player.Knight()  # If the user chose 1, the chosen character would be a knight

if build == 2:
    user = player.Assassin()  # If the user chose 2, the chosen character would be an assassin

if build == 3:
    user = player.Mage()  # If the user chose 3, the chosen character would be a mage

# This creates the game window
screenWidth = 512
screenHeight = 512
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Crawl")  # The name of the game

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
    # noinspection PyUnboundLocalVariable
    if keys[pygame.K_m]:
        user.left = False
        user.right = False
        user.up = False
        user.down = False
        user.standing = True
    if keys[pygame.K_LEFT] and (
            user.x_position - user.dex) >= 0:  # If the user presses the left arrow key, then the player moves left
        user.x_position -= user.dex
        user.left = True
        user.right = False
        user.up = False
        user.down = False
        user.standing = False
    elif keys[pygame.K_RIGHT] and (
            user.x_position + user.dex) <= screenWidth:  # If the user presses the right arrow key, then the player moves right
        user.x_position += user.dex
        user.left = False
        user.right = True
        user.up = False
        user.down = False
        user.standing = False
    elif keys[pygame.K_UP] and (
            user.y_position - user.dex) >= 0:  # If the user presses the up arrow key, then the player moves up
        user.y_position -= user.dex
        user.left = False
        user.right = False
        user.up = True
        user.down = False
        user.standing = False
    elif keys[pygame.K_DOWN] and (
            user.y_position + user.dex) <= screenHeight:  # If the user presses the down arrow key, then the player moves down
        user.y_position += user.dex
        user.left = False
        user.right = False
        user.up = False
        user.down = True
        user.standing = False
    else:
        user.standing = True
        user.walk_count = 0

    redraw_game_window()

pygame.quit()
