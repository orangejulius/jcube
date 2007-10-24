from cube import *
c=Cube()
c.display()
c.load("corners.cube");
c.display()
#cn=c.U()
c.Uprime().display()
c.U().display()

##test rotations
#test=[['a','b','c'],['d','e','f'],['g','h','i']]
#for i in range(3):
	#for j in range(3):
		#print test[i][j],
	#print

#rotateFace(test)
#for i in range(3):
	#for j in range(3):
		#print test[i][j],
	#print
#rotateFacePrime(test)
#for i in range(3):
	#for j in range(3):
		#print test[i][j],
	#print