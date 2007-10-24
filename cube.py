#represents a cube state

import copy

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
		newcube=copy.deepcopy(self)
		newcube.up=rotateFace(newcube.up)
		newslice=rotateSlice([newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]])
		newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube
	
	def Uprime(self):
		newcube=copy.deepcopy(self)
		newcube.up=rotateFacePrime(newcube.up)
		newslice=rotateSlicePrime([newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]])
		newcube.front[0],newcube.left[0],newcube.back[0],newcube.right[0]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube

	def D(self):
		newcube=copy.deepcopy(self)
		newcube.down=rotateFace(newcube.down)
		newslice=rotateSlice([newcube.left[2],newcube.front[2],newcube.right[2],newcube.back[2]])
		newcube.left[2],newcube.front[2],newcube.right[2],newcube.back[2]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube

	def Dprime(self):
		newcube=copy.deepcopy(self)
		newcube.down=rotateFacePrime(newcube.down)
		newslice=rotateSlicePrime([newcube.left[2],newcube.front[2],newcube.right[2],newcube.back[2]])
		newcube.left[2],newcube.front[2],newcube.right[2],newcube.back[2]=newslice[0],newslice[1],newslice[2],newslice[3]
		return newcube

	def L(self):
		newcube=copy.deepcopy(self)
		return newcube

	def Lprime(self):
		newcube=copy.deepcopy(self)
		return newcube

	def F(self):
		newcube=copy.deepcopy(self)
		return newcube

	def Fprime(self):
		newcube=copy.deepcopy(self)
		return newcube

	def R(self):
		newcube=copy.deepcopy(self)
		return newcube

	def Rprime(self):
		newcube=copy.deepcopy(self)
		return newcube

	def B(self):
		newcube=copy.deepcopy(self)
		return newcube

	def Bprime(self):
		newcube=copy.deepcopy(self)
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
				prettyprint(self.up[i][j])
			print
		for i in range(self.size):
			for j in range(self.size):
				prettyprint(self.left[i][j])

			for j in range(self.size):
				prettyprint(self.front[i][j])

			for j in range(self.size):
				prettyprint(self.right[i][j])

			for j in range(self.size):
				prettyprint(self.back[i][j])
			print

		for i in range(self.size):
			print "     ",
			for j in range(self.size):
				prettyprint (self.down[i][j])
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

#print using colors!
def prettyprint(out):
	if (out=='W'):
		print 'W',
	elif (out=='G'):
		print '\033[0;32m'+'G'+'\033[0m',
	elif (out=='B'):
		print '\033[1;34m'+'B'+'\033[0m',
	elif (out=='O'):
		print '\033[1;31m'+'O'+'\033[0m',
	elif (out=='Y'):
		print '\033[33m'+'Y'+'\033[0m',
	elif (out=='R'):
		print '\033[1;38m'+'R'+'\033[0m',
	else:
		print "e",#rror