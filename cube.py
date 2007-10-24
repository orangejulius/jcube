#represents a cube state
class Cube:
	def __init__(self):
		self.size=3
		
		#initialize matricies
		self.up=[["W" for col in range(self.size)] for row in range(self.size)]
		self.down=[['B' for col in range(self.size)] for row in range(self.size)]
		self.left=[['G' for col in range(self.size)] for row in range(self.size)]
		self.front=[['R' for col in range(self.size)] for row in range(self.size)]
		self.right=[['Y' for col in range(self.size)] for row in range(self.size)]
		self.back=[['O' for col in range(self.size)] for row in range(self.size)]
			
	def isValid(self):
		return True;
	
	#load state from file
	#one line per row with
	#three lines per face
	#order: up, down, left, front, right, back
	#comments are allowed: first character of line must be '#'
	#not case sensitive
	
	def load(self, filename):
		file=open(filename,'r')
		linenum=0
		rows=[]
		for line in file:
			if (line[0]!='#'):
				line=line.upper()
				line=line.strip()
				line=line.split(" ",3)
				if (len(line)!=3):
					print "error"
				#print line
				rows.append(line)
				linenum=linenum+1
		print rows
		
	#displays the cube in a compact format
	#top is displayed on top,
	#front is the center face
	#down face is on the bottom
	def display(self):
		for i in range(self.size):
			print "     ",
			for j in range(self.size):
				print self.up[i][j],
			print
		for i in range(self.size):
			for j in range(self.size):
				print self.left[i][j],

			for j in range(self.size):
				print self.front[i][j],

			for j in range(self.size):
				print self.right[i][j],

			for j in range(self.size):
				print self.back[i][j],
			print
		
		for i in range(self.size):
			print "     ",
			for j in range(self.size):
				print self.down[i][j],
			print
		