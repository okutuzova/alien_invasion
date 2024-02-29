import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing one alien"""

    def __init__(self, ai_settings, screen):
        """Initializes an alien and defines its initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # downloads alien image and appoints rect attribute
        self.image = pygame.image.load('/Users/Morgenstern/PycharmProjects/alien_invasion/images/ufo-297549_1280.bmp')
        self.image = pygame.transform.scale(self.image, (70, 60))
        self.rect = self.image.get_rect()

        # each new alien appears in the upper left screen side
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving exact alien position
        self.x = float(self.rect.x)


    def blitme(self):
        """Shows alien in a current position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if an alien is next to the screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves an alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x