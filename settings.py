class Settings:
    """Class for keeping all settings for the Alien Invasion game"""

    def __init__(self):
        """Initializes game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 128)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        # game speed up
        self.speedup_scale = 1.1

        # alien price increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings changing during game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.4

        # fleet direction: 1 - right, -1 - left
        self.fleet_direction = 1

        # score count
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed and aliens price"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)