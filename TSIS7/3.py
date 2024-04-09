import pygame
import os



pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
pygame.mixer.music.load('h.mp3')
pygame.mixer.music.play(0)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        

        
        pygame.display.flip()
        clock.tick(60)