class Settings():
    screen_width=0
    screen_height=0
    bg_color = (0,0,0)
    def  __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (87,250,255)

        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        #self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 255,60,60
        self.bullets_allowed = 100

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.ship_speed_factor= 1.5

        self.fleet_dirction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

