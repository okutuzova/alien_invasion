import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class representing one star"""

    def __init__(self, ai_settings, screen):
        """Initializes a star and defines its initial position"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # downloads star image and appoints rect attribute
        self.image = pygame.image.load('/Users/Morgenstern/PycharmProjects/alien_invasion/images/star-5786426_640.bmp')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()


    def blitme(self):
        """Shows star in a current position"""
        self.screen.blit(self.image, self.rect)
