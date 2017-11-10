import pygame, sys, time
from pygame.locals import *
from random import *

pygame.init()

(width,height) = (350,195)
screen = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Color Picker')

blue = [0,0,255]
black = [0,0,0]
white = [255,255,255]

#set colors
def colorValue(r,g,b):
    return [r,g,b]

def randomColor():
    return [randint(0,255),randint(0,255),randint(0,255)]

screen.fill(blue)

#draw 10 rows by 10 columns of squares in random colors
def changeColors():
    for i in range(0,10):
        for j in range(0,10):
            rect = Rect([i*20,j*20,10,10])
            pygame.draw.rect(screen,randomColor(),rect,0)

changeColors()

#draw three squares of white to be the textfield
def drawWhites():
    pygame.draw.rect(screen,white,[243,18,100,25],0)
    pygame.draw.rect(screen,white,[243,67,100,25],0)
    pygame.draw.rect(screen,white,[243,115,100,25],0)

drawWhites()

#draw text 'r','g','b' next to the white squares
pygame.font.init()
myfont = pygame.font.SysFont('sans-serif',40)
txtR = myfont.render('R',False,black)
txtG = myfont.render('G',False,black)
txtB = myfont.render('B',False,black)

screen.blit(txtR,(220,18))
screen.blit(txtG,(220,67))
screen.blit(txtB,(220,115))

pygame.display.update()

def getMousePos(x1,y1,x2,y2):
    mousePos = pygame.mouse.get_pos()
    return (mousePos[0] > x1 and mousePos[0] < y1 and mousePos[1] > x2 and mousePos[1] < y2)

def drawText(color):
    txtRValue = myfont.render(str(color[0]),False,black)
    txtGValue = myfont.render(str(color[1]),False,black)
    txtBValue = myfont.render(str(color[2]),False,black)
    
    screen.blit(txtRValue, (243,18) )    
    screen.blit(txtGValue, (243,67) )
    screen.blit(txtBValue, (243,115) )

#when the user hovers over a square, print the color value to the screen
#if the user hovers off the square, erase the color value from the screen
def userHover():
    drawWhites()
    colorValues = screen.get_at( pygame.mouse.get_pos() )
    for i in range(0,11):
        for j in range(0,11):
            if(colorValues[0] == 0 and colorValues[1] == 0 and colorValues[2] == 255):
                drawWhites()
            if(getMousePos(i*20,j*20,i*20,j*20)):
                colorValues = screen.get_at( pygame.mouse.get_pos() )
                drawText(colorValues)

    #there are two ways to accomplish this
        #1. get the positions of the individual squares, and see if the mouse
                #position is within those squares,
                #if it is not blue, draw the text to the screen
        #2. get any color value within the screen
                #if it is not blue,black,or white, draw the text to the screen
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    userHover()

    #let the user change the colors of the squares
    if(event.type == pygame.KEYDOWN):
           if(event.key == pygame.K_SPACE):
               changeColors()
               time.sleep(0.01)

    pygame.display.update()

pygame.exitonclose()
