#EASY LEVEL
#imports

import pygame
import math
import random

pygame.init() 

clock = pygame.time.Clock()  #to set the frame rate

#screen size
width = 1600
height = 900
display = pygame.display.set_mode((width,height))

#colors
black = (0, 0, 0)
pink = (255, 204, 230)
blue = (153, 221, 255)
green = (102, 255, 102)
purple = (102, 140, 255)
orange = (255,179,102)

colors = [pink, blue, green, purple, orange]

#globals
state = 'main menu'

cx = random.randint(20, width -20)
cy = random.randint(20, height -20)
radius = random.randint(14, 20)

#circle
pygame.draw.circle(display, random.choice(colors), (cx, cy), radius)

#main loop
while True:
    for event in pygame.event.get(): #quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    if state == 'main menu':
        #display main menu
        state = 'game'

    if state == 'game':
        #display game
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        click = pygame.mouse.get_pressed()

        sqx = (x - cx)**2
        sqy = (y - cy)**2

        if math.sqrt(sqx + sqy) < radius and click[0] == 1:
            display.fill(black) #reset screen
            cx = random.randint(20, width -20)
            cy = random.randint(20, height -20)
            radius = random.randint(14, 20)
            pygame.draw.circle(display, random.choice(colors), (cx, cy), radius)

        pygame.display.update()
        clock.tick()


