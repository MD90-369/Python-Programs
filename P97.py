#To roll the dice till the user wishes
from random import randint

roll = ''

while (roll.lower() != 'x'):

	rand_num = randint(1, 6)
	print('Dice Roll ->', rand_num)
	
	roll= input('Do you want to roll the dice again? Press any key to continue. X for exit.')