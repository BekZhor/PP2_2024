import pygame
from pygame.locals import *
import sys
import random
import time
import math

pygame.init()
z = 0
a = 400
b = 600

Monitor = pygame.display.set_mode((a, b))


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 5

Monitor.fill(WHITE)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)


pygame.display.set_caption("AnimatedStreet.png")

# Create a class for the monster car
class monster_car(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,560), 0)

    def move(self):
        self.rect.move_ip(1, 10) 
        if (self.rect.bottom > 600) :
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


# Create a class for the coin
class coin(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,560), 0)

    def move(self):
        self.rect.move_ip(1, 10) 
        if (self.rect.bottom > 600) :
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


# Create a class for the player car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < a:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    # Define the draw function for the player car
    def draw(self, surface):
        surface.blit(self.image, self.rect) 



P1 = Player()
M1 = monster_car()
C1 = coin()

monsters = pygame.sprite.Group()
monsters.add(M1)

coins = pygame.sprite.Group()
coins.add(C1)

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()

# Add the player car to the all_sprites group
all_sprites.add(P1)

# Add the monster car to the all_sprites group
all_sprites.add(M1)

# Add the coin to the all_sprites group
all_sprites.add(C1)

# Create an event to increase the speed of the cars
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True :
   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    all_sprites.update()

    
    Monitor.fill(WHITE)

   
    scores = font_small.render(str(z), True, BLACK)
    Monitor.blit(scores, (10,10))

    # Draw all the sprites in the group
    for entity in all_sprites:
        Monitor.blit(entity.image, entity.rect)

 

    # Check if the player car has collided with any of the monster cars
    if pygame.sprite.spritecollideany(P1, monsters):
          
          Monitor.fill(RED)
          
          # Update the display
          pygame.display.update()
          
          # Kill all the sprites in the group
          for entity in all_sprites:
                entity.kill() 
                
          # Wait for 2 seconds
          time.sleep(2)
          print(math.ceil(z/12))
          # Quit pygame and exit the program
          pygame.quit()
          sys.exit() 
          

    
    if pygame.sprite.spritecollideany(P1, coins):
          pygame.mixer.Sound('4204231ae09939c.mp3').play()
          z = z + 1
          
          # Update the display
          pygame.display.update()



    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
   
    P1.update()
    M1.move()
    C1.move()



    Monitor.fill(WHITE)
    P1.draw(Monitor)
    M1.draw(Monitor)
    C1.draw(Monitor)
         

        
    pygame.display.update()
    frequency = pygame.time.Clock()
    frequency.tick(60)