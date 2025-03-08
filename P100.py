#To calculate amount after compound interest
from math import pow
P = int(input("Enter principle amount:"))
T = int(input("Enter time in years:"))
R = int(input("Enter rate of interest:"))
R /= 100
temp = pow(1+R, T)
A = P*temp
print('Your compound interest is:', A)
