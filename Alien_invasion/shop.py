import pygame

class Ship():

    def __init__(self, screen):
        """init ship and set the position"""
        self.screen = screen

        # load the ship and get the size
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put ship in the centre of boot
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw ship in the certain position"""
        self.screen.blit(self.image,self.rect)