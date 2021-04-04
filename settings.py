class Settings() :
	def __init__(self) :
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0,0,0)
		
		self.ship_speed_factor = 1.7
		
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 230, 230, 230
		self.bullets_allowed = 6
		
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1