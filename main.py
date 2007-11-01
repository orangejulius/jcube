from cube import *
from CubeProblem import *
from search import *
import time

c=Cube()

quit=False
print "welcome!"
while (quit==False):
	c.display()
	text=raw_input("Enter command (h for help): ")
	command=text.split()
	if (len(command)>0):
		if (command[0]=='h'):
			print "Command list: "
			print "h: display this help"
			print "q: quit program"
			print "load [filename]: load a cube state from the given file"
			print "reset: reset the cube"
			print "scramble [num]: apply [num] random moves to make things more interesting :)"
			print "solve: solve the cube"
			print "additionally any move or rotation command may be used (ex: F or F')"
		elif (command[0]=='q'):
			quit=True
		elif (command[0]=='reset'):
			c=Cube()
		elif (command[0]=='load'):
			if (len(command)>1):
				c.load(command[1])
			else:
				print "error: no filename specified!"
		elif (command[0]=='solve'):
			t=time.clock()
			p=CubeProblem(c)
			something=astar_search(p).path()
			something.reverse()
			t=time.clock()-t
			
			print "Cube solved in "+repr(len(something)-1)+" moves!"
			print "solution took "+repr(t)
			print repr(p.appended)+ " nodes searched"
			if (t>0):
				print repr(p.appended/t)+" nodes per second"
			print "Solution: ",
			for i in something:
				if (i.action!=None):
					print i.action,
			print
		elif (command[0]=='scramble'):
			if (len(command)>1):
				if(command[1].isdigit()):
					num=int(command[1])
				else:
					num=30
			else:
				num=30
			print "applied:",
			for i in range(num):
				move=random.choice(['U','D','L','R','F','B','U\'','D\'','L\'','R\'','F\'','B\''])#,'X','Y','Z','X\'','Y\'','Z\''])
				print move,
				c=c.text2Move(move)
			print
		else:
			c=c.text2Move(command[0])