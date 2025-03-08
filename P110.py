#To accept 3 sides of 3 triangles and calculate the total area.
from math import sqrt

def area(P,Q,R):
	S = (P+Q+R)/2
	Result = sqrt(S*(S-P)*(S-Q)*(S-R))
	return Result

total_area = 0

for i in range(3):
	A = int(input(f"Enter the side a of triangle {i+1} :"))
	B = int(input(f"Enter the side b of triangle {i+1} :"))
	C = int(input(f"Enter the side c of triangle {i+1} :"))
	Result = area(A,B,C)
	print(f"Area of triangle {i+1} :", Result)
	total_area += Result

print("Total area :", total_area)
