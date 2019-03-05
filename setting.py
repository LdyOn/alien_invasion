class Setting():
	"""存储游戏设置"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (230,230,230)
		
		#子弹设置
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (69,100,155)
		self.bullet_allowed = 5

		
		self.fleet_drop_speed = 5
		
								 
		self.ship_limit = 3
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()



	def initialize_dynamic_settings(self):
		#飞船移动速度
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 0.5
		self.fleet_drection = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points*self.score_scale)

		

		

		