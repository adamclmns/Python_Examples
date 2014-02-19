#Quadratic Formula#
#Adam Clemons#

from math import sqrt
print("Given A,B, and C, I can solve equations in the form")
print("Ax^2+Bx+C=0")
A=float(input("What's A: "))
B=float(input("What's B: "))
C=float(input("What's C: "))

#Using math library to determine the discriminant#
disc1=(B**2)-(4*A*C)
if disc1<0:
	print("This function has imaginary roots")
	disc=sqrt((B**2)-(4*A*C))
	X1=(0-B+disc)/(2*A)
	X2=(0-B-disc)/(2*A)
	print("X1 is ",X1,"/n and X2 is ",X2)
else:
	disc=sqrt((B**2)-(4*A*C))
	#Putting the discriminant over 2A#
	X1=(0-B+disc)/(2*A)
	X2=(0-B-disc)/(2*A)
	#outputting the results#
	print("X1 is ",X1,"/n and X2 is ",X2)
