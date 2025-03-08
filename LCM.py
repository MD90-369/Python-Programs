# To calculate LCM of 2 numbers.

def lcm(x, y):
	num = max(x, y)

	while( num / min(x, y) != 0):
		num += max(x, y)
	
	return num