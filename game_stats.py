class GameStats():
    """Following game statistics"""

    def __init__(self, ai_settings):
        """Statistics initialization"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # game starts as inactive
        self.game_active = False

    def reset_stats(self):
        """Initialzes statistics changing during game"""
        self.ships_left = self.ai_settings.ship_limit