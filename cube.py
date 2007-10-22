class Cube:
	def __init__(self):
		self.size=3
		
		#initialize matricies
		self.up=[['W' for col in range(self.size)] for row in range(self.size)]
		self.down=[['B' for col in range(self.size)] for row in range(self.size)]
		self.left=[['G' for col in range(self.size)] for row in range(self.size)]
		self.front=[['R' for col in range(self.size)] for row in range(self.size)]
		self.right=[['Y' for col in range(self.size)] for row in range(self.size)]
		self.back[['O' for col in range(self.size)] for row in range(self.size)]
		