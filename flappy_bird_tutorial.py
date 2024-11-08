import pygame
from pygame.locals import *

pygame.init()

clock=pygame.time.Clock()
fps=60

#Screen size
screen_width=864
screen_height=800
screen = pygame.display.set_mode((screen_width,screen_height))

# Set title
pygame.display.set_caption('flappy bird')

#define game variables
ground_scroll=0
scroll_speed=4

#load images
bg=pygame.image.load('img/bg.png')
ground_img=pygame.image.load('img/ground.png')

#Set the game to run indefinitely
run = True
#While the game is running, check event. If event is Quit
while run:
    #Control how fast the code run
    clock.tick(fps)

    # Draws one surface to another
    screen.blit(bg,(0,0))

    # Draws the ground and make it scroll
    screen.blit(ground_img,(ground_scroll,768))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 35:
        ground_scroll=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()


pygame.quit()