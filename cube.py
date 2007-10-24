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

	#moves
	#these all return a new cube object with the requested move executed
	def U(self):
		newcube=Cube()
		newcube.up=rotateFace(self.up)
		newslice=rotateSlice([self.front[0],self.left[0],self.back[0],self.right[0]])
		newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube
	
	def Uprime(self):
		newcube=Cube()
		newcube.up=rotateFacePrime(self.up)
		newslice=rotateSlicePrime([self.front[0],self.left[0],self.back[0],self.right[0]])
		newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube

	def D(self):
		newcube=Cube()
		newcube.up=rotateFace(self.up)
		return newcube

	def Dprime(self):
		newcube=Cube()
		newcube.up=rotateFacePrime(self.up)
		return newcube

	def L(self):
		newcube=Cube()
		return newcube

	def Lprime(self):
		newcube=Cube()
		return newcube

	def F(self):
		newcube=Cube()
		return newcube

	def Fprime(self):
		newcube=Cube()
		return newcube

	def R(self):
		newcube=Cube()
		return newcube

	def Rprime(self):
		newcube=Cube()
		return newcube

	def B(self):
		newcube=Cube()
		return newcube

	def Bprime(self):
		newcube=Cube()
		return newcube

	
	#cube rotations
	def x(self):
		return self
	def y(self):
		return self
	def z(self):
		return self
	
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

#convenience methods that take a 3x3 matrix and rotate it

#clockwise
def rotateFace(face):
	newface=face
	#corners
	newface[0][0],newface[0][2],newface[2][0],newface[2][2]=face[2][0],face[0][0],face[2][2],face[0][2]
	
	#middle edges
	newface[0][1],newface[1][2],newface[2][1],newface[1][0]=face[1][0],face[0][1],face[1][2],face[2][1]
	
	return newface

	
#counterclockwise
def rotateFacePrime(face):
	newface=face
	#corners
	face[0][0],face[0][2],face[2][0], face[2][2]=face[0][2],face[2][2],face[0][0],face[2][0]
	
	#middle edges
	newface[0][1],newface[1][2],newface[2][1],newface[1][0]=face[1][2],face[2][1],face[1][0],face[0][1]
	
	return newface

#convenience methods that take a list of 4 sides of a slice and rotate them
#be sure to pass in the slices in clockwise order around the face being rotated

#clockwise
def rotateSlice(slice):
	return [slice[3],slice[0],slice[1],slice[2]]

#counterclockwise
def rotateSlicePrime(slice):
	return [slice[1],slice[2],slice[3],slice[0]]
		