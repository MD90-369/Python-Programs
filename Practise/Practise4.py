#To print the series a,a+x,a+2x till the nth term

print('To print the series...')
print('a, a+x, a+2x, a+3x, ... till n terms \n')

a = int(input("Enter A : "))
x = int(input("Enter X: "))
num = int(input("Enter N: "))

for i in range(0, num):
	print(a+(x*i), end = ',')


