from cube import *
c=Cube()
print "1: default cube"
c.display()


print "2: loaded corners.cube file"
c.load("corners.cube");
c.display()

print "3: D rotation"
c.D().display()

print "4: D' rotation"
c.Dprime().display()

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