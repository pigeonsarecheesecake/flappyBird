import pygame
from pygame.locals import *

pygame.init()

clock=pygame.time.Clock()
fps=60

#Screen size
screen_width=864
screen_height=936
screen = pygame.display.set_mode((screen_width,screen_height))

# Set title
pygame.display.set_caption('flappy bird')

#define game variables
ground_scroll=0
scroll_speed=4

#load images
bg=pygame.image.load('img/bg.png')
ground_img=pygame.image.load('img/ground.png')

#Bird. Sprite class has its own draw functions, like i dont need blit function
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # Initiate sprite
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index = 0
        self.counter=0
        for num in range(1,4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)

        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        # Position
        self.rect.center=[x,y]

    def update(self):
        #handle the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index=0
        self.image=self.images[self.index]

bird_group=pygame.sprite.Group()

# Instance of the Bird class
flappy = Bird(100,int(screen_height/2))

# Add flappy to the bird_group
bird_group.add(flappy)

#Set the game to run indefinitely
run = True
#While the game is running, check event. If event is Quit
while run:
    #Control how fast the code run
    clock.tick(fps)

    # Draws one surface to another
    screen.blit(bg,(0,0))

    bird_group.draw(screen)
    bird_group.update()

    # Draws the ground and make it scroll, in reality it just brings the image back to its original position
    screen.blit(ground_img,(ground_scroll,768))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 35:
        ground_scroll=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()


pygame.quit()