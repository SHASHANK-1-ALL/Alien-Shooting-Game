class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

        # High score should never be reset
        filename = 'High_Score.txt'
        with open(filename) as file_object:
            val = file_object.read()
        self.high_score = int(val)

    def reset_stats(self):
        """Initializing stats that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1