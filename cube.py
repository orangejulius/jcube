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
	
	#double moves
	def F2():
		return self.F().F()
	def B2():
		return self.B().B()
	def L2():
		return self.L().L()
	def R2():
		return self.R().R()
	def U2():
		return self.U().U()
	def D2():
		return self.D().D()
	
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
	
	#converts a text command to the appropriate function call
	def text2Move(self, command):#
		if (command=='F'):
			return self.F()
		elif (command=='F\''):
			return self.Fprime()
		elif (command=='B'):
			return self.B()
		elif (command=='B\''):
			return self.Bprime()
		elif (command=='U'):
			return self.U()
		elif (command=='U\''):
			return self.Uprime()
		elif (command=='D'):
			return self.D()
		elif (command=='D\''):
			return self.Dprime()
		elif (command=='L'):
			return self.L()
		elif (command=='L\''):
			return self.Lprime()
		elif (command=='R'):
			return self.R()
		elif (command=='R\''):
			return self.Rprime()
		elif (command=='X'):
			return self.X()
		elif (command=='X\''):
			return self.Xprime()
		elif (command=='Y'):
			return self.Y()
		elif (command=='Y\''):
			return self.Yprime()
		elif (command=='Z'):
			return self.Z()
		elif (command=='Z\''):
			return self.Zprime()
		else:
			print "command "+command+" unknown!"
			return self

	#determine if this state is equivalent to the goal state
	#most of the work is orienting the cube correctly
	def isGoal(self):
		#first move red face to front
		test=copy.deepcopy(self)#make a copy so we don't alter the cube
		if (test.up[1][1]=='R'):
			test=test.Xprime()
		elif (test.down[1][1]=='R'):
			test=test.X()
		elif (test.left[1][1]=='R'):
			test=test.Yprime()
		elif (test.right[1][1]=='R'):
			test=test.Y()
		elif (test.back[1][1]=='R'):
			test=test.Y().Y()
		elif (test.front[1][1]!='R'):
			print "couldn't find red face! this is bad!"
			return False

		#now move the white face to the top		
		if (test.down[1][1]=='W'):
			test=test.Z().Z()
		elif (test.left[1][1]=='W'):
			test=test.Zprime()
		elif (test.right[1][1]=='W'):
			test=test.Z()
		elif (test.up[1][1]!='W'):
			print "couldn't find white face! this is bad!"
			return False

		#now do some comparing
		goal=Cube()#goal state cube
		for i in range(3):
			for j in range(3):
				if goal.up[i][j]!=test.up[i][j]:
					return False
				if goal.down[i][j]!=test.down[i][j]:
					return False
				if goal.left[i][j]!=test.left[i][j]:
					return False
				if goal.right[i][j]!=test.right[i][j]:
					return False
				if goal.front[i][j]!=test.front[i][j]:
					return False
				if goal.back[i][j]!=test.back[i][j]:
					return False
		return True
			
	def heuristic(self):
		count=0
		for i in range(3):
			for j in range(3):
				if self.up[i][j]!=self.up[1][1]:
					count=count+1
				if self.down[i][j]!=self.down[1][1]:
					count=count+1
				if self.left[i][j]!=self.left[1][1]:
					count=count+1
				if self.right[i][j]!=self.right[1][1]:
					count=count+1
				if self.front[i][j]!=self.front[1][1]:
					count=count+1
				if self.back[i][j]!=self.back[1][1]:
					count=count+1
		#return float(count)/5.
		return count/5
	
	def cornersInPlace(self):
		count=8
		#front left up
		if (self.front[0][0]==self.front[1][1]) & (self.left[0][2]==self.left[1][1]) & (self.up[2][0]==self.up[1][1]):
			count=count-1
			
		#front right up
		if (self.front[0][2]==self.front[1][1]) & (self.right[0][0]==self.right[1][1]) & (self.up[2][2]==self.up[1][1]):
			count=count-1
			
		#front left down
		if (self.front[2][0]==self.front[1][1]) & (self.left[2][2]==self.left[1][1]) & (self.down[0][0]==self.down[1][1]):
			count=count-1
			
		#front right down
		if (self.front[2][2]==self.front[1][1]) & (self.right[2][0]==self.right[1][1]) & (self.down[0][2]==self.down[1][1]):
			count=count-1
			
		#back left up
		if (self.back[0][2]==self.back[1][1]) & (self.left[0][0]==self.left[1][1]) & (self.up[0][0]==self.up[1][1]):
			count=count-1
			
		#back right up
		if (self.back[0][0]==self.back[1][1]) & (self.right[0][2]==self.right[1][1]) & (self.up[0][2]==self.up[1][1]):
			count=count-1
			
		#back left down
		if (self.back[2][2]==self.back[1][1]) & (self.left[2][0]==self.left[1][1]) & (self.down[2][0]==self.down[1][1]):
			count=count-1
		#back right down
		if (self.back[2][0]==self.back[1][1]) & (self.right[2][2]==self.right[1][1]) & (self.down[2][2]==self.down[1][1]):
			count=count-1
		return count
		
	def edgesInPlace1(self):
		count=6
		#front up
		if (self.front[0][1]==self.front[1][1]) & (self.up[2][1]==self.up[1][1]):
			#print "FU"
			count=count-1
			
		#left up
		if (self.left[0][1]==self.left[1][1]) & (self.up[1][0]==self.up[1][1]):
			#print "LU"
			count=count-1
		#right up
		if (self.right[0][1]==self.right[1][1]) & (self.up[1][2]==self.up[1][1]):
			#print "RU"
			count=count-1
		#back up
		if (self.back[0][1]==self.back[1][1]) & (self.up[0][1]==self.up[1][1]):
			#print "BU"
			count=count-1
		
		#front left
		if (self.front[1][0]==self.front[1][1]) & (self.left[1][2]==self.left[1][1]):
			#print "FL"
			count=count-1
		#front right
		if (self.front[1][2]==self.front[1][1]) & (self.right[1][0]==self.right[1][1]):
			#print "FR"
			count=count-1
		return count

	def edgesInPlace2(self):
		count=6
		#front down
		if (self.front[2][1]==self.front[1][1]) & (self.down[0][1]==self.down[1][1]):
			#print "FD"
			count=count-1
		
		#left down
		if (self.left[2][1]==self.left[1][1]) & (self.down[1][0]==self.down[1][1]):
			#print "LD"
			count=count-1
			
		#right down
		if (self.right[2][1]==self.right[1][1]) & (self.down[1][2]==self.down[1][1]):
			#print "RD"
			count=count-1
			
		#back down
		if (self.back[2][1]==self.back[1][1]) & (self.down[2][1]==self.down[1][1]):
			#print "BD"
			count=count-1
			
		#back left
		if (self.back[1][2]==self.back[1][1]) & (self.left[1][0]==self.left[1][1]):
			#print "BL"
			count=count-1
			
		#back right
		if (self.back[1][0]==self.back[1][1]) & (self.right[1][2]==self.right[1][1]):
			#print "BR"
			count=count-1
			
		return count
		
	def heuristic2(self):
		h1=self.cornersInPlace()
		if h1==0:
			h2=self.edgesInPlace1()
			if (h2==0):
				return h2
			else:
				return self.edgesInPlace1()
		else:
			return h1
		
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