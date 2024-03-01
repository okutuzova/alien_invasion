class GameStats():
    """Following game statistics"""

    def __init__(self, ai_settings):
        """Statistics initialization"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # game starts as inactive
        self.game_active = False

        # record cannot be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialzes statistics changing during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1