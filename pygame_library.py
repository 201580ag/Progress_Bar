import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 50))
pygame.display.set_caption("Progress Bar")

progress = 0

while progress < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (0, 128, 255), (0, 0, progress * 40, 50))
    pygame.display.update()
    progress += 1
    pygame.time.delay(100)