import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Button attributes initialization"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Defining size and features
        self.width, self.height = 200, 50
        self.button_color = (143, 188, 143)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Building button rect object and center alignment
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message is created once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Makes msg a rectangular and aligns in center"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Placing empty button and message output"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)