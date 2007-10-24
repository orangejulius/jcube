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
	
	#moves
	def U(self):
		return self
	def Uprime(self):
		return self
	def D(self):
		return self
	def Dprime(self):
		return self
	def L(self):
		return self
	def Lprime(self):
		return self
	def F(self):
		return self
	def Fprime(self):
		return self
	def R(self):
		return self
	def Rprime(self):
		return self
	def B(self):
		return self
	def Bprime(self):
		return self
	
	#cube rotations
	def x(self):
		return self
	def y(self):
		return self
	def z(self):
		return self
	
	#convenience methods that take a 3x3 matrix and rotate it
	def rotateFace(self,face):
		
	def rotateFacePrime(self,face):
	
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
			if (line[0]!='#'):#check if this line is a comment
				line=line.upper()
				line=line.strip()
				line=line.split(" ",3)
				if (len(line)!=3):
					print "error: wrong number of characters on line"
					return False;
				#print line
				rows.append(line)
				linenum=linenum+1
		if (linenum!=18):
			print "error: wrong number of lines"
			return False;
		else:
			self.up=rows[:3]
			self.down=rows[3:6]
			self.left=rows[6:9]
			self.front=rows[9:12]
			self.right=rows[12:15]
			self.back=rows[15:18]
			return True;

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