from cube import *
c=Cube()

quit=False
print "welcome!"
while (quit==False):
	c.display()
	command=raw_input("Enter command (h for help): ")
	if (command=='h'):
		print "Command list: "
		print "h: display this help"
		print "q: quit program"
		print "load: load a cube state from a file"
		print "reset: reset the cube"
		print "additionally any move or rotation command may be used (ex: F or F')"
	elif (command=='q'):
		quit=True
	elif (command=='reset'):
		c=Cube()
	elif (command=='load'):
		filename=raw_input("Enter filename: ")
		c.load(filename)
	elif (command=='F'):
		c=c.F()
		c.display()
	elif (command=='F\''):
		c=c.Fprime()
		c.display()
	elif (command=='B'):
		c=c.B()
		c.display()
	elif (command=='B\''):
		c=c.Bprime()
		c.display()
	elif (command=='U'):
		c=c.U()
		c.display()
	elif (command=='U\''):
		c=c.Uprime()
		c.display()
	elif (command=='D'):
		c=c.D()
		c.display()
	elif (command=='D\''):
		c=c.Dprime()
		c.display()
	elif (command=='L'):
		c=c.L()
		c.display()
	elif (command=='L\''):
		c=c.Lprime()
		c.display()
	elif (command=='R'):
		c=c.R()
		c.display()
	elif (command=='R\''):
		c=c.Rprime()
		c.display()
	elif (command=='X'):
		c=c.X()
		c.display()
	elif (command=='X\''):
		c=c.Xprime()
		c.display()
	elif (command=='Y'):
		c=c.Y()
		c.display()
	elif (command=='Y\''):
		c=c.Yprime()
		c.display()
	elif (command=='Z'):
		c=c.Z()
		c.display()
	elif (command=='Z\''):
		c=c.Zprime()
		c.display()
	else:
		print "command "+command+" unknown!"
	
	

##tests
#print "1: default cube"
#c.display()

#print "2: loaded corners.cube file"
#c.load("scrambled.cube");
#c.display()

#print "3: X rotation"
#c.X().display()

#print "4: X' rotation"
#c.Xprime().display()

#print "5: should be the same as 2"
#c.display()

