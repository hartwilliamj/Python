import random

def roll(sides):
	num_rolled = random.randint(1,sides)
	return num_rolled

def main():
	sides = 6
	rolling = True
	while rolling:
		roll_again = input("Had enough yet? ENTER=roll. Q=quit")
		if roll_again.lower() != "q":
			num_rolled = roll(sides)
			print("You rolled a ", num_rolled)
		else:
			rolling = False
			print("Later sucker")

main()