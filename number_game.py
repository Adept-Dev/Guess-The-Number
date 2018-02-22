# Guess the Number Game

import random

def randnum():
	num_gen = random.randint(1,4)
	return num_gen

guess = int(input("Guess a number between 1 and 25."))

def main():
	num = randnum()
	while guess != num:
		incorrect = int(input("Wrong number. Try again!"))
		print(incorrect)
	else:	
		print("Congrats you won!")	

main()	