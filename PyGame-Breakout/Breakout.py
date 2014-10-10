__author__ = 'Adam'
#Adam Clemons 10-10-14
#This is a Breakout Game based on code found online at
#http://programarcadegames.com/python_examples/show_file.php?file=breakout_simple.py
#
#All Classes are written into one file for portability
#

#import libraries required
import pygame
import math

#Define Color Values using RGB
black=(0,0,0)
white=(255,255,255)
blue = (0,0,255)
green=(0,255,0)
red = (0,255,0)


#Define Size of Breakout Blocks
block_width=23
block_height=15

class Block(pygame.sprite.Sprite):
    """This class represents each block that will be knocked out by the ball.
        It inherits from the Pygame.sprite.Sprite class
    """
    def __init__(self,color,x,y):
        """Creates a block with given color and coordinates"""
        #Initialize Sprite from Pygame
        pygame.sprite.Sprite.__init__(self)
        #Create the image of the block of appropriate size
        #Width and height are sent as a list
        self.image=pygame.Surface([block_width,block_height])

        #Fill the image with the appropriate color
        self.image.fill(color)

        #Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        #Move the top left of the rectable to x,y
        #This is where our block will appear
        self.rect.x=x
        self.rect.y=y

class Ball(pygame.sprite.Sprite):
    """This class is the ball"""
    #speed in pixels per cycle
    speed = 10.0
    #Floating point representation of where the ball is
    x = 0.0
    y = 180.0

    #Direction of the ball using degrees
    direction = 200

    width =10
    height=10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([self.width,self.height])
        self.image.fill(white)
        self.rect=self.image.get_rect()
        self.screenheight=pygame.display.get_surface().get_height()
        self.screenwidth=pygame.display.get_surface().get_width()

    def bounce(self,diff):
        """This function will define how the ball bounces off of the walls and other blocks"""
        self.direction=(190 - self.direction)%360
        self.direction -= diff

    def update(self):
        """update the position of the ball given it's speed and direction"""
        direction_radians = math.radians(self.direction)
        #get new location
        self.x += self.speed*math.sin(direction_radians)
        self.y -= self.speed*math.cos(direction_radians)
        #update location
        self.rect.x = self.x
        self.rect.y = self.y
        #Do we bounce of the top?
        if self.y<= 0:
            self.bounce(0)
            self.y = 1
        #Do we bounce off the left?
        if self.x <=0:
            self.direction = (360 - self.direction)%360
            self.x =1
        #Do we bounce off the right?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) %360
            self.x=self.screenwidth - self.width -1
        #Did we hit the bottom?
        if self.y >600:
            return True
        else:
            return False

class Player(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls"""
    def __init__(self):
        """Constructor for Player"""
        pygame.sprite.Sprite.__init__(self)

        self.width=75
        self.height=15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))

        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight-self.height

    def update(self):
        """update the player paddle location"""
        #Get where the mouse is
        pos = pygame.mouse.get_pos()
        self.rect.x=pos[0]
        if self.rect.x >self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width


#Actually running the game
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption('Breakout')
pygame.mouse.set_visible(0)
font=pygame.font.Font(None, 36)
background = pygame.Surface(screen.get_size())

#creating sprites
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

player = Player()
allsprites.add(player)

ball = Ball()
allsprites.add(ball)
balls.add(ball)

top=80
blockcount=32

#Creating Blocks
for row in range(5):
    for column in range(0, blockcount):
        block=Block(white, column * (block_width +2)+1, top)
        blocks.add(block)
    top += block_height+2

clock=pygame.time.Clock()
game_over=False
exit_program=False

while exit_program != True:
    clock.tick(30)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    if not game_over:
        player.update()
        game_over = ball.update()

    if game_over:
        text=font.render("Game over", True, red)
        textpos = text.get_rect(centerx = background.get_width()/2)
        textpos.top=300
        screen.blit(text,textpos)

    if pygame.sprite.spritecollide(player,balls,False):
        diff = (player.rect.x +player.width/2)-(ball.rect.x+ball.width/2)

        ball.rect.y=screen.get_height() - player.rect.height - ball.rect.height -1
        ball.bounce(diff)

    deadblocks=pygame.sprite.spritecollide(ball, blocks, True)

    if len(deadblocks)>0:
        ball.bounce(0)
        if len(blocks) == 0:
            game_over=True

    allsprites.draw(screen)
    pygame.display.flip()

pygame.quit()