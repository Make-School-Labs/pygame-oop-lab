import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
surface = pygame.Surface(screen.get_size())

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    background = pygame.Rect((0, 0), screen.get_size())
    pygame.draw.rect(surface, pygame.Color('white'), background)

    r = pygame.Rect((x, y), (100, 100))
    pygame.draw.rect(surface, pygame.Color('blue'), r)
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60)

    x += 1
    y += 1

