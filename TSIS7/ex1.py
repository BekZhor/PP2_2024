import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()

left_arm = pygame.image.load('leftarm.jpeg')
right_arm = pygame.image.load('rightarm.jpeg')
clock_image = pygame.image.load('mainclock.jpeg')

w, h = clock_image.get_size()

angle = 360
rangle = 360

done = False

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    screen.fill(0)

    rotated_clock = pygame.transform.rotate(clock_image, 0)
    rotated_clock_rect = rotated_clock.get_rect(center=pos)

    # Получение текущего времени
    now = datetime.datetime.now()


    # Вычисление угла поворота для секундной стрелки
    seconds = now.second
    seconds_angle = 360 * seconds / 60


    # Вычисление угла поворота для минутной стрелки
    minutes = now.minute
    minutes_angle = 360 * minutes / 60 + seconds_angle / 60


   
    # Поворот и отображение стрелок
    rotated_left_arm = pygame.transform.rotate(left_arm, -seconds_angle)
    rotated_left_arm_rect = rotated_left_arm.get_rect(center=pos)


    rotated_right_arm = pygame.transform.rotate(right_arm, -minutes_angle)
    rotated_right_arm_rect = rotated_right_arm.get_rect(center=pos)


    screen.blit(rotated_clock, rotated_clock_rect)
    screen.blit(rotated_left_arm, rotated_left_arm_rect)
    screen.blit(rotated_right_arm, rotated_right_arm_rect)
 


    pygame.display.flip()

pygame.quit()