import pygame
import time
import random
pygame.init()
disw=800
dish=600
gameDisplay=pygame.display.set_mode((disw,dish))
pygame.display.set_caption('Ultraa')
pygame.display.update()
white=(255,255,255)
black=(0,0,0)
green=(0,155,0)
red=(255,0,0)
block=20
direction='right'
ablock=20
FPS=20
img=pygame.image.load('snakehead.png')
icon=pygame.image.load('apple_icon.png')
apple=pygame.image.load('apple_1.png')
pygame.display.set_icon(icon)
small=pygame.font.SysFont('comicsansms',25)
medium=pygame.font.SysFont('comicsansms',50)
large=pygame.font.SysFont('comicsansms',80)



def text_objects(msg,color,size):
    if size=='small':
        textsurface=small.render(msg,True,color)
    elif size=='medium':
        textsurface=medium.render(msg,True,color)
    elif size=='large':
        textsurface=large.render(msg,True,color)
    return textsurface,textsurface.get_rect()
def message(msg,color,y_displace=0,size='small'):
    textsurface,textrect=text_objects(msg,color,size)
    textrect.center=(disw/2),(dish/2)+y_displace
    gameDisplay.blit(textsurface,textrect)
clock=pygame.time.Clock()

def score(score):
    text=small.render('Score :'+str(score),True,black)
    gameDisplay.blit(text,[0,0])
def intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message('Welcome to Snake',red,y_displace=-80,size='large')
        pygame.display.update()
        clock.tick(5)
            
def snake(block,snakelist):
    if direction=='right':
        shead=pygame.transform.rotate(img,270)
    elif direction=='left':
        shead=pygame.transform.rotate(img,90)
    elif direction=='down':
        shead=pygame.transform.rotate(img,180)
    elif direction=='up':
        shead=img
    gameDisplay.blit(shead,(snakelist[-1][0],snakelist[-1][1]))
    for index in snakelist[:-1]:
        gameDisplay.fill(green,rect=[index[0],index[1],block,block])
    
def gameLoop():
    global direction
    direction='right'
    gameexit=True
    gameOver=False
    x=disw/2
    y=dish/2
    snakelist=[]
    snakecount=2
    rand_x=random.randrange(0,disw-block,10)
    rand_y=random.randrange(0,dish-block,10)
    x1=10
    y1=0
            
    while gameexit:
        
        while gameOver==True:
            gameDisplay.fill(white)
            message('Game Over',red,y_displace=-50,size='large')
            message('Choose q to quit and c to play gain!',black,y_displace=50,size='small')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameexit=False
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver= False
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1=-block
                    y1=0
                    direction='left' 
                elif event.key==pygame.K_RIGHT:
                    x1=block
                    y1=0
                    direction='right' 
                elif event.key==pygame.K_DOWN:
                    y1=block
                    x1=0
                    direction='down' 
                elif event.key==pygame.K_UP:
                    y1=-block
                    x1=0
                    direction='up' 
        if x>=disw-block or x<0 or y>= dish-block or y<0:
                gameOver=True
        if len(snakelist)>snakecount:
            del snakelist[0]
        x+=x1
        y+=y1
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)

        if snakehead in snakelist[:-1]:
            if snakehead == snakelist[0]:
                continue
            gameOver = True

        if x>=rand_x and x<=rand_x+ablock or x+block>=rand_x and x+block<=rand_x+ablock:
            if y>=rand_y and y<=rand_y+ablock or y+block>=rand_y and y+block<=rand_y+ablock:
                rand_x=random.randrange(0,disw-block,10)
                rand_y=random.randrange(0,dish-block,10)
                snakecount+=1           
        gameDisplay.fill(white)
        gameDisplay.blit(apple,(rand_x,rand_y,ablock,ablock))
        snake(block,snakelist)
        score(snakecount-2) 
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

intro()
gameLoop()
