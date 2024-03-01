import pygame.font


class Scoreboard():
    """Class to output game info"""
    def __init__(self, ai_settings, screen, stats):
        """Initializing attributes for score count"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # fonts settings
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # preparing start pic
        self.prep_score()

    def prep_score(self):
        """Transforms current score in pic"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Score output right upper screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Score output in the screen"""
        self.screen.blit(self.score_image, self.score_rect)
