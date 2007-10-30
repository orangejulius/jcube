from cube import *
import random
c=Cube()

quit=False
print "welcome!"
while (quit==False):
	c.display()
	text=raw_input("Enter command (h for help): ")
	command=text.split()
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
	elif (command[0]=='solve'):
		print c.isGoal()
	elif (command[0]=='scramble'):
		if (command[1].isdigit()):
			print "applied:",
			for i in range(int(command[1])):
				move=random.choice(['U','D','L','R','F','B','X','Y','Z','U\'','D\'','L\'','R\'','F\'','B\'','X\'','Y\'','Z\''])
				print move,
				c=c.text2Move(move)
			print
		else:
			print "please enter an integer number "
	else:
		c=c.text2Move(command[0])