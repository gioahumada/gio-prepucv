import pygame
import random

SCREEN_WEIGHT = 960
SCREEN_HEIGHT = 960

COLOR_BLACK = (0, 0 , 0)
COLOR_WHITE = (255, 255, 255)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WEIGHT))

    pygame.display.set_caption('GioPong')

    while True:
        screen.fill(COLOR_BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == '__main__':
    main()


