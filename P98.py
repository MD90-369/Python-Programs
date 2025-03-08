#To create a number guessing game
from random import randint

choice = ''

while (choice.lower() != 'x'):
	answer = randint(1, 1000)
	tries = 10
	guess = 0 

	while (tries > 0) and (guess != answer):
		guess = int(input(f'Guess a number between 1 and 1000. ({tries} tries left):'))

		if(guess > answer):
			print("The number is lower. Try again")
		elif(guess < answer):
			print("The number is higher. Try again")

		tries = tries - 1 

	if(tries == 0):
		print("You LOSE!!!")
	else:
		print("Congrats. You Win!!!")

	choice= input('Do you want to play again? Press any key to continue. X for exit.')