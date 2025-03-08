#To print a matrix of m * n stars
n = int(input('How many stars in a row? :'))
m = int(input('How many columns to print? :'))
ch = '*'

for _ in range(m):
	print(n * ch)