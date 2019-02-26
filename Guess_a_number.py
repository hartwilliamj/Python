import random

# Checks string (s) if there's a digit in the string ( isdigit() ) 
def is_valid_num(s):
	if s.isdigit() and 1 <= int(s) <= 100:
		return True
	else:
		return False

def main():
	number = random.randint(1,100)
	guessed_num = False
	guess = input("Guess a # between 1 and 100:   ")
	num_guesses = 0
	while not guessed_num:
		if not is_valid_num(guess):
			guess = input("That's not a # between 1 and 100... Try again:   ")
			continue
		else:
			num_guesses += 1
			guess = int(guess)

		if guess < number:
			guess = input("Too low. Guess again:   ")
		elif guess > number:
			guess = input("Too high. Guess again:   ")
		else:
			print("You got it! It only took you",num_guesses,"guesses!")
			guessed_num = True

	play_again = input("Would you like to play again? Enter = Yes. Q=quit.   ")
	while play_again.upper() != "Q":
		main()
	else:
		prin("Whatever loser, later...")

main()