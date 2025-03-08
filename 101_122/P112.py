# To calculate LCM of 3 numbers.

def lcm(x, y):
	num = max(x, y)

	while( num % min(x, y) != 0):
		num += max(x, y)
	
	return num

ch = 'a'

while (ch != 'x' and ch != 'X'):
	a = int(input("Enter 1st number:"))
	b = int(input("Enter 2nd number:"))
	c = int(input("Enter 3rd number:"))

	result = lcm(lcm(a, b), c)

	print("LCM of", a, b, c, ":", result)

	ch = input('\n(Press Any Key to Continue)\n(x to exit)\n\n')
