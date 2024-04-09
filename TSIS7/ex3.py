import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

x=30
y=30

while not done:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            y -= 20
            if y==0:
                y=300

        if pressed[pygame.K_DOWN]: 
            y += 20
            if y==300:
                y=0

        if pressed[pygame.K_LEFT]:
            x -= 20
            if x==0:
                x=400
        if pressed[pygame.K_RIGHT]: 
            x += 20
            if x==400:
                x=0


        screen.fill((0, 0, 0))
        
        pygame.draw.circle(screen, (255,0,0), (x,y) ,25)
        pygame.display.flip()
        clock.tick(60)