import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class handling bullets that a ship shoots"""

    def __init__(self, ai_settings, screen, ship):
        """Creats a bullet in ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating a bullet in position (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet's position is kept as a float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """Moves bullets"""
        # Updates bullet position
        self.y -= self.speed_factor
        # Updates rect position
        self.rect.y = self.y


    def draw_bullet(self):
        """Puts bullet on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)