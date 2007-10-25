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
		newcube.left=rotateFace(newcube.left)
		slice=[[newcube.up[0][0],newcube.up[1][0],newcube.up[2][0]]]
		slice.append([newcube.front[0][0],newcube.front[1][0],newcube.front[2][0]])
		slice.append([newcube.down[0][0],newcube.down[1][0],newcube.down[2][0]])
		slice.append([newcube.back[2][2],newcube.back[1][2],newcube.back[0][2]])
		slice=rotateSlice(slice)
		newcube.up[0][0],newcube.up[1][0],newcube.up[2][0]=slice[0]
		newcube.front[0][0],newcube.front[1][0],newcube.front[2][0]=slice[1]
		newcube.down[0][0],newcube.down[1][0],newcube.down[2][0]=slice[2]
		newcube.back[2][2],newcube.back[1][2],newcube.back[0][2]=slice[3]
		return newcube

	def Lprime(self):
		newcube=copy.deepcopy(self)
		newcube.left=rotateFacePrime(newcube.left)
		slice=[[newcube.up[0][0],newcube.up[1][0],newcube.up[2][0]]]
		slice.append([newcube.front[0][0],newcube.front[1][0],newcube.front[2][0]])
		slice.append([newcube.down[0][0],newcube.down[1][0],newcube.down[2][0]])
		slice.append([newcube.back[2][2],newcube.back[1][2],newcube.back[0][2]])
		slice=rotateSlicePrime(slice)
		newcube.up[0][0],newcube.up[1][0],newcube.up[2][0]=slice[0]
		newcube.front[0][0],newcube.front[1][0],newcube.front[2][0]=slice[1]
		newcube.down[0][0],newcube.down[1][0],newcube.down[2][0]=slice[2]
		newcube.back[2][2],newcube.back[1][2],newcube.back[0][2]=slice[3]
		return newcube

	def F(self):
		newcube=copy.deepcopy(self)
		newcube.front=rotateFace(newcube.front)
		slice=[newcube.up[2]]
		slice.append([newcube.right[0][0],newcube.right[1][0],newcube.right[2][0]])
		slice.append(newcube.down[0])
		slice[2].reverse()
		slice.append([newcube.left[2][2],newcube.left[1][2],newcube.left[0][2]])
		slice=rotateSlice(slice)
		newcube.up[2]=slice[0]
		newcube.right[0][0],newcube.right[1][0],newcube.right[2][0]=slice[1]
		newcube.down[0]=slice[2]
		newcube.down[0].reverse()
		newcube.left[2][2],newcube.left[1][2],newcube.left[0][2]=slice[3]		
		return newcube

	def Fprime(self):
		newcube=copy.deepcopy(self)
		newcube.front=rotateFacePrime(newcube.front)
		slice=[newcube.up[2]]
		slice.append([newcube.right[0][0],newcube.right[1][0],newcube.right[2][0]])
		slice.append(newcube.down[0])
		slice[2].reverse()
		slice.append([newcube.left[2][2],newcube.left[1][2],newcube.left[0][2]])
		slice=rotateSlicePrime(slice)
		newcube.up[2]=slice[0]
		newcube.right[0][0],newcube.right[1][0],newcube.right[2][0]=slice[1]
		newcube.down[0]=slice[2]
		newcube.down[0].reverse()
		newcube.left[2][2],newcube.left[1][2],newcube.left[0][2]=slice[3]
		return newcube

	def R(self):
		newcube=copy.deepcopy(self)
		newcube.right=rotateFace(newcube.right)
		slice=[[newcube.up[2][2],newcube.up[1][2],newcube.up[0][2]]]
		slice.append([newcube.back[0][0],newcube.back[1][0],newcube.back[2][0]])
		slice.append([newcube.down[2][2],newcube.down[1][2],newcube.down[0][2]])
		slice.append([newcube.front[2][2],newcube.front[1][2],newcube.front[0][2]])
		slice=rotateSlice(slice)
		newcube.up[2][2],newcube.up[1][2],newcube.up[0][2]=slice[0]
		newcube.back[0][0],newcube.back[1][0],newcube.back[2][0]=slice[1]
		newcube.down[2][2],newcube.down[1][2],newcube.down[0][2]=slice[2]
		newcube.front[2][2],newcube.front[1][2],newcube.front[0][2]=slice[3]
		return newcube

	def Rprime(self):
		newcube=copy.deepcopy(self)
		newcube.right=rotateFacePrime(newcube.right)
		slice=[[newcube.up[2][2],newcube.up[1][2],newcube.up[0][2]]]
		slice.append([newcube.back[0][0],newcube.back[1][0],newcube.back[2][0]])
		slice.append([newcube.down[2][2],newcube.down[1][2],newcube.down[0][2]])
		slice.append([newcube.front[2][2],newcube.front[1][2],newcube.front[0][2]])
		slice=rotateSlicePrime(slice)
		newcube.up[2][2],newcube.up[1][2],newcube.up[0][2]=slice[0]
		newcube.back[0][0],newcube.back[1][0],newcube.back[2][0]=slice[1]
		newcube.down[2][2],newcube.down[1][2],newcube.down[0][2]=slice[2]
		newcube.front[2][2],newcube.front[1][2],newcube.front[0][2]=slice[3]
		return newcube

	def B(self):
		newcube=copy.deepcopy(self)
		newcube.back=rotateFace(newcube.back)
		slice=[newcube.up[0]]
		slice[0].reverse()
		slice.append([newcube.left[0][0],newcube.left[1][0],newcube.left[2][0]])
		slice.append(newcube.down[2])
		slice.append([newcube.right[2][2],newcube.right[1][2],newcube.right[0][2]])
		slice=rotateSlice(slice)
		newcube.up[0]=slice[0]
		newcube.up[0].reverse()
		newcube.left[0][0],newcube.left[1][0],newcube.left[2][0]=slice[1]
		newcube.down[2]=slice[2]
		newcube.right[2][2],newcube.right[1][2],newcube.right[0][2]=slice[3]		
		return newcube

	def Bprime(self):
		newcube=copy.deepcopy(self)
		newcube.back=rotateFacePrime(newcube.back)
		slice=[newcube.up[0]]
		slice[0].reverse()
		slice.append([newcube.left[0][0],newcube.left[1][0],newcube.left[2][0]])
		slice.append(newcube.down[2])
		slice.append([newcube.right[2][2],newcube.right[1][2],newcube.right[0][2]])
		slice=rotateSlicePrime(slice)
		newcube.up[0]=slice[0]
		newcube.up[0].reverse()
		newcube.left[0][0],newcube.left[1][0],newcube.left[2][0]=slice[1]
		newcube.down[2]=slice[2]
		newcube.right[2][2],newcube.right[1][2],newcube.right[0][2]=slice[3]
		return newcube
	
	#cube rotations
	def X(self):
		newcube=copy.deepcopy(self)
		newcube.right=rotateFace(newcube.right)
		newcube.left=rotateFacePrime(newcube.left)
		newcube.front,newcube.up,newcube.back,newcube.down=newcube.down,newcube.front,newcube.up,newcube.back
		newcube.back=rotateFace(newcube.back)
		newcube.back=rotateFace(newcube.back)
		newcube.down=rotateFace(newcube.down)
		newcube.down=rotateFace(newcube.down)
		return newcube
	
	def Xprime(self):
		newcube=copy.deepcopy(self)
		newcube.right=rotateFacePrime(newcube.right)
		newcube.left=rotateFace(newcube.left)
		newcube.front,newcube.up,newcube.back,newcube.down=newcube.up,newcube.back,newcube.down,newcube.front
		newcube.up=rotateFace(newcube.up)
		newcube.up=rotateFace(newcube.up)
		newcube.back=rotateFace(newcube.back)
		newcube.back=rotateFace(newcube.back)

		return newcube
	
	def Y(self):
		newcube=copy.deepcopy(self)
		newcube.up=rotateFace(newcube.up)
		newcube.down=rotateFacePrime(newcube.down)
		newcube.front,newcube.right,newcube.back,newcube.left=newcube.right,newcube.back,newcube.left,newcube.front
		return newcube
	
	def Yprime(self):
		newcube=copy.deepcopy(self)
		newcube.up=rotateFacePrime(newcube.up)
		newcube.down=rotateFace(newcube.down)
		newcube.front,newcube.right,newcube.back,newcube.left=newcube.left,newcube.front,newcube.right,newcube.back
		return newcube
	
	def Z(self):
		newcube=copy.deepcopy(self)
		newcube.front=rotateFacePrime(newcube.front)
		newcube.back=rotateFace(newcube.back)
		newcube.up,newcube.right,newcube.down,newcube.left=newcube.right,newcube.down,newcube.left,newcube.up
		newcube.up=rotateFacePrime(newcube.up)
		newcube.right=rotateFacePrime(newcube.right)
		newcube.down=rotateFacePrime(newcube.down)
		newcube.left=rotateFacePrime(newcube.left)		
		return newcube
	
	def Zprime(self):
		newcube=copy.deepcopy(self)
		newcube.front=rotateFace(newcube.front)
		newcube.back=rotateFacePrime(newcube.back)
		newcube.up,newcube.right,newcube.down,newcube.left=newcube.left,newcube.up,newcube.right,newcube.down
		newcube.up=rotateFace(newcube.up)
		newcube.right=rotateFace(newcube.right)
		newcube.down=rotateFace(newcube.down)
		newcube.left=rotateFace(newcube.left)
		return newcube
	
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
			print "      ",
			for j in range(self.size):
				prettyprint(self.up[i][j])
			print
		for i in range(self.size):
			for j in range(self.size):
				prettyprint(self.left[i][j])
			print "",

			for j in range(self.size):
				prettyprint(self.front[i][j])
			print "",

			for j in range(self.size):
				prettyprint(self.right[i][j])
			print "",

			for j in range(self.size):
				prettyprint(self.back[i][j])
			print

		for i in range(self.size):
			print "      ",
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
#ok the colors aren't quite right for orange and yellow
def prettyprint(out):
	if 1:#change to 0 to disable pretty printing
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
			print "e",#error
	else:
		print out,