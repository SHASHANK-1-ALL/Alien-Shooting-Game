class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings if window mode
        self.screen_width = 900
        self.screen_height = 600
        # Screen Background color
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly game should speed up
        self.speedup_scale = 1.1

        # How quickly alien point values will increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initializing settings that vary as the game progresses"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet direction of 1 represents right and -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points*self.score_scale)
