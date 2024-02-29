import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initializes a ship and its start point"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading ship picture
        self.image = pygame.image.load('images/ship-8464818_1280.bmp')
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship appears next to the screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # saving center coord
        self.center = float(self.rect.centerx)

        # marks movements
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates position upon movements"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor


        # updating rect attribute based on self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draws a ship in its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places ship in bottom center"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom