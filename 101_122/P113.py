#To find all factors of a number

def factors(x):
	flist = [ ]

	for i in range(1, x+1):
		if (x % i == 0):
			flist.append(i)

	return flist

# Driver Code

num = int(input("Enter a number:"))
result = factors(num)

print("Factor of", num, ":", result)
