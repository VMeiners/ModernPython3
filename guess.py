import random

random_number = random.randint(1,10)

while guess != random_number:
	guess = input("Pick a number from 1 and 10: "):
	guess = int(guess)
	elif guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else: 
		print("YOU WON!")