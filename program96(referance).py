# To demonstrate random module

from random import random, randint, choice, shuffle, sample

# 1 : random() : Generates a random number between 0 and 1

rand_num = random()
print('random() ->', rand_num)


# 2 : randint(x, y) : Generates a random integer between x and y (inclusive)

rand_num = randint(1, 10)
print('randint() ->', rand_num)


# 3 : choice(iter) : Chooses one of many choices

fruits = ['apple', 'banana', 'orange', 'mango', 'cherry']
rand_fruit = choice(fruits)
print('choice() ->', rand_fruit)


# 4 : shuffle(iter) : Shuffles an interable (except range)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(numbers)
print('shuffle() ->', numbers)


# 5 : sample(iter, n) : picks 'n' random elements from iterable

rand_pick = sample(range(1, 11), 3)
print('sample() ->', rand_pick)
