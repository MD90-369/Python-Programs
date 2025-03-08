# To print the series:- 0,-1,2,-3,4,-5... till n no. of terms.
n = int(input('To print a series till \'n\' no. of terms. \n Enter \'n\': '))
for i in range(n):
	isOdd = (i%2 == 1)
	if isOdd:
		print(-i, end=', ')
	else:
		print(i, end=', ')
