from random import *
import pygame

pygame.init()
(width, height) = (300,260)

SCREEN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mickey Mouse")

WHITE = [255,255,255]

numColorChanges = 0
colorSequence = list()

def drawMickey(color):
    pygame.draw.circle(SCREEN, color, (150, 150), 80, 0)
    pygame.draw.circle(SCREEN, color, (90, 70), 40, 0)
    pygame.draw.circle(SCREEN, color, (203, 70), 40, 0)

def update():
    pygame.display.update()
    
drawMickey(WHITE)
update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #store random sequence into string?
    if(event.type == pygame.MOUSEBUTTONDOWN):
        randomColor = [randint(0,255),randint(0,255),randint(0,255)]
        drawMickey(randomColor)
        update()
        numColorChanges += 1
    elif(event.type == pygame.MOUSEBUTTONUP):
        update()
    elif(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_RETURN):
            print("Total number of color changes:",numColorChanges)
