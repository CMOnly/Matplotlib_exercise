import sys

import pygame

from settings import Settings


def run_game():
    #  init game and create an screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #set the color of background
    bg_color = (ai_settings.bg_color)

    # begin the mani loop of game
    while True:

        # monitor the events of mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #fill the screen
        screen.fill(bg_color)
        # display the latest screen
        pygame.display.flip()


run_game()
