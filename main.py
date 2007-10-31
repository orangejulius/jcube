from cube import *
from CubeProblem import *
from search import *

c=Cube()

quit=False
print "welcome!"
while (quit==False):
	c.display()
	print c.heuristic()
	text=raw_input("Enter command (h for help): ")
	command=text.split()
	if (len(command)>0):
		if (command[0]=='h'):
			print "Command list: "
			print "h: display this help"
			print "q: quit program"
			print "load: load a cube state from a file"
			print "reset: reset the cube"
			print "scramble [num]: apply [num] random moves to make things more interesting :)"
			print "solve: solve the cube"
			print "additionally any move or rotation command may be used (ex: F or F')"
		elif (command[0]=='q'):
			quit=True
		elif (command[0]=='reset'):
			c=Cube()
		elif (command[0]=='load'):
			filename=raw_input("Enter filename: ")
			c.load(filename)
		elif (command[0]=='goal'):
			print c.isGoal()
		elif (command[0]=='solve'):
			p=CubeProblem(c)
			something=astar_search(p)
			print "Cube solved in "+repr(len(something.path())-1)+" moves!"
			print "Actions: ",
			for i in something.path():
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
				move=random.choice(['U','D','L','R','F','B','X','Y','Z','U\'','D\'','L\'','R\'','F\'','B\'','X\'','Y\'','Z\''])
				print move,
				c=c.text2Move(move)
			print
		else:
			c=c.text2Move(command[0])