import pygame
import os

pygame.init()

screen_width = 400
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

music_directory = "y"
music_files = os.listdir(music_directory)
current_index = 0
is_playing = False

pygame.mixer.init()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


running = True
while running:
    screen.fill(WHITE)

    current_track = music_files[current_index]
    draw_text(current_track, font, BLACK, screen, 10, 10)

    play_button = pygame.Rect(50, 100, 80, 40)
    pygame.draw.rect(screen, BLACK, play_button)
    draw_text('|> / ||', font, WHITE, screen, 55, 110)

    next_button = pygame.Rect(200, 100, 80, 40)
    pygame.draw.rect(screen, BLACK, next_button)
    draw_text("->", font, WHITE, screen, 220, 110)

    prev_button = pygame.Rect(320, 100, 80, 40)
    pygame.draw.rect(screen, BLACK, prev_button)
    draw_text("<-", font, WHITE, screen, 350, 110)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_button.collidepoint(mouse_pos):
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif next_button.collidepoint(mouse_pos):
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(
                    os.path.join(music_directory, music_files[current_index])
                )
                pygame.mixer.music.play()
                is_playing = True
            elif prev_button.collidepoint(mouse_pos):
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(
                    os.path.join(music_directory, music_files[current_index])
                )
                pygame.mixer.music.play()
                is_playing = True

    pygame.display.flip()

pygame.quit()