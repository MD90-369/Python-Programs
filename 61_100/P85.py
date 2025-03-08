#To print fibonacci sequence till n no. of terms.
n = int(input('To print Fibonacci series till \'n\' no. of terms. \n Enter \'n\': '))

# 0 & 1 are starting terms
# every next term is the sum of previous 2 terms, c = a + b
a = 0
b = 1
print(a, b, end=' ')


for _ in range(n-2):	
	c = a+b
	print(c, end=' ')
	a = b
	b = c
