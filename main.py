from cube import *
c=Cube()
print "1: default cube"
c.display()

print "2: loaded corners.cube file"
c.load("scrambled.cube");
c.display()

print "3: Y rotation"
c.Y().display()

print "4: Y' rotation"
c.Yprime().display()

print "5: should be the same as 2"
c.display()

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