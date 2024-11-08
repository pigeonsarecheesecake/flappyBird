import pygame
from pygame.locals import *

pygame.init()

#Screen size
screen_width=864
screen_height=936
screen = pygame.display.set_mode((screen_width,screen_height))
# Set title
pygame.display.set_caption('flappy bird')

#Set the game to run indefinitely
run = True
#While the game is running, check event. If event is Quit
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


pygame.quit()