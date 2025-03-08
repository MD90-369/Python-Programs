#To calculate area of a triangle using heron's formula
from math import sqrt
while True:
	try:
		A = int(input("Enter the side a of triangle:"))
		B = int(input("Enter the side b of triangle:"))
		C = int(input("Enter the side c of triangle:"))
		S = (A+B+C)/2
		area = sqrt(S*(S-A)*(S-B)*(S-C))
	except ValueError:
		print('Please enter a valid number only.')
	else:
		print("Area of triangle:", area)
		break
