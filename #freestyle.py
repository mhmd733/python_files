#freestyle
import pygame
import random 
import math
import time
pygame.init()
WIDTH, HEIHT = 800, 600
WIN =pygame.display.set_mode((WIDTH,HEIHT))
pygame.display.set_caption("Fuck yaaaaah")

TERGET_INC = 400
TERGET_EVENT = pygame.USEREVENT
TERGET_PADDING = 30

BG_COLOR = (0,25,40)
class Target :
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    def update (self):
        if self.size  + self.GROWTH_RATE >= self.MAX_SIZE : 
            self.grow = False      
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR,
                           (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR,
                           (self.x, self.y), self.size * 0.4)   
    def collide (self,x,y):
      dis =  math.sqrt((self.x-x )**2 + (self.y-y)**2)
      return dis <= self.size 

def draw(win,targets):
    win.fill(BG_COLOR)
    for target in targets :
        target.draw(win)

    pygame.display.update()    
def Main():




    run = True 
    targets = []
    clock = pygame.time.Clock()

    terget_pressed = 0
    clicks = 0
    mises = 0
    start_time = time.time()


    pygame.time.set_timer(TERGET_EVENT,TERGET_INC)
    while run:
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
            if event.type == TERGET_EVENT :
                x = random.randint(TERGET_PADDING,WIDTH-TERGET_PADDING)
                y = random.randint(TERGET_PADDING,HEIHT-TERGET_PADDING)
                target = Target(x,y)
                targets.append(target) 
            if event.type == pygame.MOUSEBUTTONDOWN  :
                click = True 
                clicks += 1 

                  
    for target in targets :
        target.update()

        if target.size <=0 :
         targets.remove(target)
         
        if click and  target.collide(*mouse_pos):
           targets.remove(target)
           terget_pressed += 1
    
    
    
    draw(WIN,targets)
    pygame.quit()


if __name__ == "__main__"  :
  Main()  