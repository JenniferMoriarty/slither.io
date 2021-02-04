#Slither Game
#Coded by Logan, 1/20/2021
import pygame #imports
import math #needed for square root funtion
import random

pygame.init()
pygame.display.set_caption("Slither")
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

doExit = False

#Player varibles
xPos = 200
yPos= 200
Vx = 1
Vy = 1

class pellet:
    def __init__ (self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)
    def collide(self, x ,y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < self.radius + 6:
            self.xpos = random.randrange(0,400)
            self.ypos = random.randrange(0,400)
            self.red = random.randrange(0,255)
            self.blue = random.randrange(0,255)
            self.green = random.randrange(0,255)
            self.radius = random.randrange(3,30)
            return True
class TailSeg:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def update(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (200, 0, 0), (self.xpos, self.ypos), 12)
        
oldX = 200
oldY = 100
counter = 0
        
pelletBag = list()
tail = list()
    
for i in range(100):
    pelletBag.append(pellet(random.randrange(0,400), random.randrange(0,400), random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), random.randrange(3,30)))
    

#gameloop
while not doExit:
    
    #event/input
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            
            if mousePos[0]>xPos:
                Vx = 1
            else:
                Vx = -1
            
            if mousePos[1]>yPos:
                Vy = 1
            else:
                Vy = -1
    
    #physics section
    xPos += Vx
    yPos += Vy
    
    counter+=1
    if counter == 20:
        counter = 0
        oldX = xPos
        oldY = yPos
        
        if(len(tail)>2):
            for i in range(len(tail)):
                tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
                tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
            
        if(len(tail)>0):
            tail[0].update(oldX, oldY)
    
    for i in range(100):
        if pelletBag[i].collide(xPos, yPos) == True:
            tail.append(TailSeg(oldX, oldY))
    
    #render
    screen.fill((255,255,255))
    
    pygame.draw.circle(screen, (200, 0 ,200), (xPos, yPos), 12)
    
    for i in range(100):
        pelletBag[i].draw()
        
    for i in range(len(tail)):
        tail[i].draw()
    
    pygame.display.flip()
    
pygame.quit()    
